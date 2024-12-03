from dscs.repository import Repository

def main():
    repo = Repository()

    # Initialize the repository
    repo.init_repository()

    # Create and add a file to the staging area
    with open('testfile1.txt', 'w') as f:
        f.write('Hello, DSCS - First Commit!')
    repo.add_file('testfile1.txt')
    repo.commit("First commit of testfile1.txt")

    # Create and commit another file in the feature branch
    repo.create_branch('feature-branch')
    repo.switch_branch('feature-branch')
    with open('testfile2.txt', 'w') as f:
        f.write('Hello from feature branch!')
    repo.add_file('testfile2.txt')
    repo.commit("Feature branch commit with testfile2.txt")

    # Switch back to master and merge the feature branch
    repo.switch_branch('master')
    repo.merge('feature-branch')

    # Clone the repository
    repo.clone('cloned_repo')

    # View commit history
    repo.log()

if __name__ == "__main__":
    main()
