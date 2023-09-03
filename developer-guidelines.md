1. Code Quality:
   - Before committing any changes, developers must run `make lint` on the base directory to ensure code quality and adherence to coding standards.
   - The linting process should check for syntax errors, code formatting, and other potential issues.

2. Testing:
   - Developers are required to add tests for each module or function they create or modify.
   - Tests should cover different scenarios and edge cases to ensure the reliability and correctness of the code.
   - Test cases should be written using a suitable testing framework like pytest or unittest.

3. Version Control:
   - Developers should use Git for version control and follow the Git Conventional Commits guidelines.
   - Each commit message should have a clear and concise description of the changes made.
   - Commits should be atomic and focused on a single logical change.
   - Branches should be created for new features or bug fixes, and pull requests should be used for code review and merging.
   
   > Conventional Commits
    - Commit messages MAY use Conventional Commits format. It provides guidelines to create a better commit history log, making easier to have automated tasks around it (e.g. automated changelogs). Commits would follow the format <type>[optional scope]: <description>, where <type> might be feat/fix/chore/docs etc. and breaking changes are indicated on the beginning of the optional body or footer section. [Git commits](https://github.com/naming-convention/naming-convention-guides/blob/master/git/commit-message-naming.md)

4. Documentation:
   - Code should be well-documented using appropriate comments and docstrings.
   - Functions, classes, and modules should have clear and descriptive docstrings explaining their purpose, inputs, and outputs.
   - Any external dependencies or requirements should be documented, including installation instructions if necessary.
