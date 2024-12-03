from dscs.repository import Repository

def main():
    repo = Repository()

    # Initialize the repository
    repo.init_repository()

    # Create and add a file to the staging area
    with open('pesapaldoc1.txt', 'w') as f:
        f.write('Hello, Pesa pal software Gurus, - First Commit!')
    repo.add_file('pesapaldoc1.txt')
    repo.commit("First commit of pesapaldoc1.txt")

    # Create and commit another file in the feature branch
    repo.create_branch('PesaPal2024SourceControlSystem')
    repo.switch_branch('PesaPal2024SourceControlSystem')
    with open('pesapaldoc2.txt', 'w') as f:
        f.write('Hello World?!!!!')
    repo.add_file('pesapaldoc2.txt')
    repo.commit("Feature branch commit with pesapaldoc2.txt")

    # Switch back to master and merge the feature branch
    repo.switch_branch('master')
    repo.merge('PesaPal2024SourceControlSystem')

    # Clone the repository(you can change here to new diff repo)
    repo.clone('new_cloned_repo')

    # View commit history
    repo.log()

if __name__ == "__main__":
    main()
