import os
import hashlib
import shutil
import time

class Repository:
    def __init__(self, repo_dir='.dscs'):
        self.repo_dir = repo_dir
        self.objects_dir = os.path.join(self.repo_dir, 'objects')
        self.refs_dir = os.path.join(self.repo_dir, 'refs', 'heads')
        self.head_file = os.path.join(self.repo_dir, 'HEAD')

    def init_repository(self):
        """Initialize a new DSCS repository."""
        if os.path.exists(self.repo_dir):
            print("Repository already initialized.")
            return

        os.makedirs(self.objects_dir)
        os.makedirs(self.refs_dir)

        # Create initial index file and HEAD pointing to master branch
        with open(os.path.join(self.repo_dir, 'index'), 'w') as f:
            f.write('')
        with open(self.head_file, 'w') as f:
            f.write('refs/heads/master')

        # Create an initial empty branch file
        with open(os.path.join(self.refs_dir, 'master'), 'w') as f:
            f.write('')

        print("Repository initialized successfully.")

    def hash_object(self, data):
        """Create a hash of the given data."""
        sha1 = hashlib.sha1()
        sha1.update(data)
        return sha1.hexdigest()

    def add_file(self, file_path):
        """Add a file to the staging area."""
        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist.")
            return

        with open(file_path, 'rb') as f:
            content = f.read()

        file_hash = self.hash_object(content)

        # Store the file content in the .dscs/objects directory
        object_path = os.path.join(self.objects_dir, file_hash)
        with open(object_path, 'wb') as obj_file:
            obj_file.write(content)

        # Add the file path and hash to the .dscs/index file
        with open(os.path.join(self.repo_dir, 'index'), 'a') as index_file:
            index_file.write(f"{file_path} {file_hash}\n")

        print(f"File '{file_path}' added to staging area.")

    def commit(self, message):
        """Commit the staged changes."""
        with open(os.path.join(self.repo_dir, 'index'), 'r') as f:
            index_content = f.read().strip()

        if not index_content:
            print("No files to commit.")
            return

        commit_hash = self.hash_object(index_content.encode() + message.encode())
        commit_content = f"{message}\n{index_content}\n{time.time()}\n"

        # Save the commit object
        with open(os.path.join(self.objects_dir, commit_hash), 'w') as commit_file:
            commit_file.write(commit_content)

        # Update the current branch to point to the new commit
        branch = self._get_current_branch()
        with open(os.path.join(self.refs_dir, branch), 'w') as branch_file:
            branch_file.write(commit_hash)

        # Clear the index
        with open(os.path.join(self.repo_dir, 'index'), 'w') as f:
            f.write('')

        print(f"Committed changes with message: '{message}'.")

    def log(self):
        """Display the commit history."""
        branch = self._get_current_branch()
        branch_file = os.path.join(self.refs_dir, branch)

        if not os.path.exists(branch_file):
            print("No commits found.")
            return

        with open(branch_file, 'r') as f:
            commit_hash = f.read().strip()

        while commit_hash:
            commit_file = os.path.join(self.objects_dir, commit_hash)
            if not os.path.exists(commit_file):
                break
            with open(commit_file, 'r') as f:
                commit_content = f.read()
                print(f"Commit {commit_hash}:\n{commit_content}\n")
            break

    def _get_current_branch(self):
        """Get the current branch from HEAD."""
        with open(self.head_file, 'r') as f:
            return f.read().strip().split('/')[-1]

    def _get_current_commit(self):
        """Get the current commit hash of the current branch."""
        branch = self._get_current_branch()
        branch_file = os.path.join(self.refs_dir, branch)
        if os.path.exists(branch_file):
            with open(branch_file, 'r') as f:
                return f.read().strip()
        return ''

    def create_branch(self, branch_name):
        """Create a new branch."""
        current_commit = self._get_current_commit()
        branch_file = os.path.join(self.refs_dir, branch_name)
        with open(branch_file, 'w') as f:
            f.write(current_commit)
        print(f"Branch '{branch_name}' created.")

    def switch_branch(self, branch_name):
        """Switch to another branch."""
        branch_file = os.path.join(self.refs_dir, branch_name)
        if not os.path.exists(branch_file):
            print(f"Branch '{branch_name}' does not exist.")
            return

        with open(self.head_file, 'w') as f:
            f.write(f"refs/heads/{branch_name}")
        print(f"Switched to branch '{branch_name}'.")

    def merge(self, branch_name):
        """Merge the given branch into the current branch."""
        branch_file = os.path.join(self.refs_dir, branch_name)
        if not os.path.exists(branch_file):
            print(f"Branch '{branch_name}' does not exist.")
            return

        with open(branch_file, 'r') as f:
            branch_commit = f.read().strip()

        current_commit = self._get_current_commit()

        if current_commit == branch_commit:
            print(f"Already up to date with branch '{branch_name}'.")
        else:
            self.commit(f"Merge branch '{branch_name}' into '{self._get_current_branch()}'")
            print(f"Branch '{branch_name}' merged.")

    def clone(self, target_dir):
        """Clone the current repository to a new target directory."""
        if not os.path.exists(self.repo_dir):
            print(f"Repository not initialized at '{self.repo_dir}'. Nothing to clone.")
            return

        if os.path.exists(target_dir):
            print(f"Target directory '{target_dir}' already exists.")
            return

        print(f"Cloning repository from '{self.repo_dir}' to '{target_dir}'...")
        shutil.copytree(self.repo_dir, os.path.join(target_dir, '.dscs'))
        
        # Verify if cloning was successful
        if os.path.exists(os.path.join(target_dir, '.dscs')):
            print(f"Cloned repository structure in '{target_dir}':")
            print(os.listdir(os.path.join(target_dir, '.dscs')))
        else:
            print(f"Cloning failed. '{target_dir}/.dscs' does not exist.")
        
        print(f"Repository cloned to '{target_dir}' successfully.")
