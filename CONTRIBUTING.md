
## CONTRIBUTING.md

Thank you for considering contributing to this project! Here are some guidelines to help make the contribution process smooth and efficient.

### Table of Contents
- [Code Style](#code-style)
- [Branching Strategy](#branching-strategy)
- [Commit Message Convention](#commit-message-convention)
- [Pull Requests](#pull-requests)
- [Code of Conduct](#code-of-conduct)

---

### Code Style
Please follow the Django and PEP8 coding conventions:
- **Indentation**: Use 4 spaces for indentation.
- **Naming**: Use `snake_case` for variables and functions, `CamelCase` for class names.
- **Imports**: Group imports into three sections: standard library, third-party libraries, and local Django imports.

### Branching Strategy
- **main**: This branch contains stable code.
- **feature/your-feature-name**: For new features or enhancements.
- **bugfix/description**: For bug fixes.

Always branch from `main` and create a new branch for each feature or fix.

### Commit Message Convention
For consistent commit messages, use the following structure and prefixes:

1. **Type**:
   - **feat**: A new feature
   - **fix**: A bug fix
   - **docs**: Documentation changes
   - **style**: Code formatting, missing semi-colons, etc.
   - **refactor**: Refactoring code without adding new features
   - **test**: Adding or updating tests
   - **chore**: Updates to tasks, configurations, or dependencies

2. **Format**:
   Use the format `type: Short description` for commit messages. Keep the description under 50 characters, and provide more details in the body if needed.

3. **Examples**:
   - `feat: Add user login and registration`
   - `fix: Correct API response status code for errors`
   - `docs: Update README with setup instructions`
   - `style: Adjust spacing in views.py`
   - `test: Add unit tests for user profile`

### Pull Requests
1. Ensure your feature or bug fix is thoroughly tested.
2. Open a pull request (PR) against the `main` branch with a clear description.
3. Link any relevant issues in the PR description.
4. Request a review and make necessary updates based on feedback.

### Code of Conduct
This project follows a [Code of Conduct](CODE_OF_CONDUCT.md) to ensure a welcoming and inclusive environment.

---

Thank you for contributing! Your efforts help make this project better for everyone.