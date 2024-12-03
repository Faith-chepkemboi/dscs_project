import os
import hashlib
import time
import shutil

class Repository:
    def __init__(self, repo_dir='.dscs'):
        self.repo_dir = repo_dir
        self.ignore_file = '.ignore'  # Default ignore file name

    def init_repository(self):
        """Initialize a new DSCS repository."""
        if os.path.exists(self.repo_dir):
            print("Repository already initialized.")
            return

        # Create necessary directories and files for the repository
        os.makedirs(self.repo_dir)
        os.makedirs(os.path.join(self.repo_dir, 'objects'))
        os.makedirs(os.path.join(self.repo_dir, 'refs', 'heads'))

        # Create initial index file and HEAD pointing to master branch
        with open(os.path.join(self.repo_dir, 'index'), 'w') as f:
            f.write('')

        with open(os.path.join(self.repo_dir, 'HEAD'), 'w') as f:
            f.write('refs/heads/master')

        # Create the initial empty commit for the master branch
        self.create_initial_commit()

        print("Repository initialized successfully.")

    def hash_object(self, data):
        """Create a SHA-1 hash of the given data."""
        sha1 = hashlib.sha1()
        sha1.update(data)
        return sha1.hexdigest()

    def add_file(self, file_path):
        """Add a file to the staging area, respecting the .ignore file."""
        # Check if the file is in the ignore list
        if self.is_file_ignored(file_path):
            print(f"File '{file_path}' is ignored based on .ignore rules.")
            return

        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist.")
            return

        with open(file_path, 'rb') as f:
            content = f.read()

        file_hash = self.hash_object(content)

        # Store the file content in the .dscs/objects directory
        object_path = os.path.join(self.repo_dir, 'objects', file_hash)
        with open(object_path, 'wb') as obj_file:
            obj_file.write(content)

        # Add the file path and hash to the .dscs/index file
        with open(os.path.join(self.repo_dir, 'index'), 'a') as index_file:
            index_file.write(f"{file_path} {file_hash}\n")

        print(f"File '{file_path}' added to staging area.")

    def is_file_ignored(self, file_path):
        """Check if the file is ignored based on the .ignore file."""
        if not os.path.exists(self.ignore_file):
            return False  # No ignore file, so don't ignore anything

        with open(self.ignore_file, 'r') as ignore_file:
            ignore_patterns = ignore_file.readlines()

        # Check each pattern in the ignore file
        for pattern in ignore_patterns:
            pattern = pattern.strip()
            if pattern and file_path.endswith(pattern):
                return True

        return False

    def get_current_branch(self):
        """Get the current branch from HEAD."""
        head_path = os.path.join(self.repo_dir, 'HEAD')
        with open(head_path, 'r') as f:
            ref = f.read().strip()
        return ref.split('/')[-1]

    def get_parent_commit(self):
        """Get the hash of the parent commit."""
        branch = self.get_current_branch()
        branch_path = os.path.join(self.repo_dir, 'refs', 'heads', branch)
        if os.path.exists(branch_path):
            with open(branch_path, 'r') as f:
                return f.read().strip()
        return None

    def create_initial_commit(self):
        """Create an initial commit for the master branch."""
        commit_hash = self.hash_object(b'Initial commit')
        branch_path = os.path.join(self.repo_dir, 'refs', 'heads', 'master')
        with open(branch_path, 'w') as f:
            f.write(commit_hash)

    def commit(self, message):
        """Commit the staged files."""
        index_path = os.path.join(self.repo_dir, 'index')
        if not os.path.exists(index_path) or os.stat(index_path).st_size == 0:
            print("Nothing to commit.")
            return

        # Read the index file (staged files)
        with open(index_path, 'r') as f:
            index_data = f.read()

        parent_commit = self.get_parent_commit()
        timestamp = int(time.time())

        # Create commit metadata
        commit_content = f"parent {parent_commit}\n" if parent_commit else ''
        commit_content += f"timestamp {timestamp}\n"
        commit_content += f"message {message}\n"
        commit_content += f"files:\n{index_data}"

        # Hash and store the commit
        commit_hash = self.hash_object(commit_content.encode())
        commit_path = os.path.join(self.repo_dir, 'objects', commit_hash)
        with open(commit_path, 'w') as f:
            f.write(commit_content)

        # Update the current branch to point to the new commit
        branch = self.get_current_branch()
        branch_path = os.path.join(self.repo_dir, 'refs', 'heads', branch)
        with open(branch_path, 'w') as f:
            f.write(commit_hash)

        # Clear the index after committing
        open(index_path, 'w').close()

        print(f"Commit '{commit_hash}' created successfully.")

    def log(self):
        """Display the commit history."""
        branch = self.get_current_branch()
        branch_path = os.path.join(self.repo_dir, 'refs', 'heads', branch)
        if not os.path.exists(branch_path):
            print(f"Branch '{branch}' does not exist.")
            return

        # Read the current commit hash from the branch reference
        current_commit_hash = open(branch_path).read().strip()

        print(f"Commit history for branch '{branch}':\n")

        # Traverse the commit history
        while current_commit_hash:
            commit_path = os.path.join(self.repo_dir, 'objects', current_commit_hash)
            if not os.path.exists(commit_path):
                print(f"Commit object {current_commit_hash} does not exist.")
                break

            with open(commit_path, 'r') as f:
                commit_content = f.read()

            # Extract commit metadata and files
            lines = commit_content.splitlines()
            parent_commit = [line for line in lines if line.startswith('parent')]
            timestamp = [line for line in lines if line.startswith('timestamp')]
            message = [line for line in lines if line.startswith('message')]
            files = [line for line in lines if line.startswith('files:')]

            print(f"Commit {current_commit_hash}:")
            print(f"  Message: {message[0].split(' ', 1)[1]}")
            print(f"  Timestamp: {timestamp[0].split(' ', 1)[1]}")
            if parent_commit:
                print(f"  Parent: {parent_commit[0].split(' ', 1)[1]}")

            print(f"  Files:")
            for line in files[0:]:
                print(f"    {line}")

            # Move to the next commit (parent commit)
            current_commit_hash = parent_commit[0].split(' ', 1)[1] if parent_commit else None
            print("\n")

    def create_branch(self, branch_name):
        """Create a new branch."""
        branch_path = os.path.join(self.repo_dir, 'refs', 'heads', branch_name)
        if os.path.exists(branch_path):
            print(f"Branch '{branch_name}' already exists.")
            return

        current_commit_hash = self.get_parent_commit()
        with open(branch_path, 'w') as f:
            f.write(current_commit_hash)

        print(f"Branch '{branch_name}' created successfully.")

    def switch_branch(self, branch_name):
        """Switch to an existing branch."""
        branch_path = os.path.join(self.repo_dir, 'refs', 'heads', branch_name)
        if not os.path.exists(branch_path):
            print(f"Branch '{branch_name}' does not exist.")
            return

        # Update HEAD to point to the new branch
        with open(os.path.join(self.repo_dir, 'HEAD'), 'w') as f:
            f.write(f"refs/heads/{branch_name}")

        print(f"Switched to branch '{branch_name}'.")

    def list_branches(self):
        """List all branches."""
        branches_dir = os.path.join(self.repo_dir, 'refs', 'heads')
        if not os.path.exists(branches_dir):
            print("No branches found.")
            return

        branches = os.listdir(branches_dir)
        print("Branches:")
        for branch in branches:
            print(f"  {branch}")

    def merge(self, branch_to_merge):
        """Merge the given branch into the current branch."""
        current_branch = self.get_current_branch()
        if branch_to_merge == current_branch:
            print(f"You are already on branch '{current_branch}'. No need to merge.")
            return

        # Get the commit hashes of both branches
        current_branch_commit = self.get_parent_commit()
        merge_branch_commit = open(os.path.join(self.repo_dir, 'refs', 'heads', branch_to_merge)).read().strip()

        # Simple conflict detection (if same file is modified in both branches)
        conflicts = self.check_conflicts(current_branch_commit, merge_branch_commit)
        if conflicts:
            print(f"Conflicts detected in the following files:")
            for conflict in conflicts:
                print(f"  {conflict}")
            return

        # Perform the merge (for simplicity, just update the current branch with the merge branch commit)
        with open(os.path.join(self.repo_dir, 'refs', 'heads', current_branch), 'w') as f:
            f.write(merge_branch_commit)

        print(f"Successfully merged '{branch_to_merge}' into '{current_branch}'.")

    def check_conflicts(self, branch1_commit, branch2_commit):
        """Check for conflicts between two branches."""
        # For simplicity, we will assume a conflict occurs if both branches have modified the same file
        # (This is a simplified conflict detection and would need to be more advanced in a full implementation)
        return ["pesapalRegdoc1.txt", "pesapalRegdoc2.txt"]  # Placeholder for conflicting files

    def clone(self, target_dir):
        """Clone the repository to a new directory."""
        if os.path.exists(target_dir):
            print(f"The directory {target_dir} already exists. Cannot clone here.")
            return

        # Copy all the repository contents to the target directory
        shutil.copytree(self.repo_dir, target_dir)
        print(f"Repository successfully cloned to {target_dir}.")
