## 🌟 CONTRIBUTING.md

Thank you for contributing to our project! Your input helps improve this project and its community. To make contributions smooth, please review the guidelines below.

### Table of Contents
- [👩‍💻 Code Style](#-code-style)
- [🌿 Branching Strategy](#-branching-strategy)
- [💬 Commit Message Convention](#-commit-message-convention)
- [📦 Adding Features and Files](#-adding-features-and-files)
- [📥 Pull Requests](#-pull-requests)
- [🤝 Code of Conduct](#-code-of-conduct)

---

### 👩‍💻 Code Style
Please follow these coding standards to keep the codebase clean and consistent:
- **Indentation**: Use 4 spaces for indentation.
- **Naming**: Use `snake_case` for variables and functions, `CamelCase` for class names.
- **Imports**: Group imports in three sections: standard library, third-party libraries, and local Django imports.

### 🌿 Branching Strategy
- **`main`**: Stable, production-ready code.
- **`feature/your-feature-name`**: New features or enhancements.
- **`bugfix/description`**: Bug fixes.

🔄 **Always branch off from `main`** and create a new branch for each feature or fix.

### 💬 Commit Message Convention
For consistent and readable commit history, use the following format and add emojis to represent the change type.

1. **Types of Changes**:
   - 🚀 **feat**: A new feature or enhancement.
   - 🐛 **fix**: A bug fix.
   - 📄 **docs**: Changes to documentation.
   - 🎨 **style**: Code style changes (formatting, etc.).
   - ♻️ **refactor**: Code changes without adding features or fixing bugs.
   - ✅ **test**: Adding or updating tests.
   - 🔧 **chore**: Config updates, dependency changes, etc.
   - 📦 **build**: Build scripts, CI changes, or dependency updates.

2. **Format**:
   Use `type: Short description` for commit messages. Keep it concise (under 50 characters if possible) and avoid a period at the end.

3. **Examples**:
   - 🚀 `feat: Add user login functionality`
   - 🐛 `fix: Correct URL paths in app config`
   - 📄 `docs: Update README with setup instructions`
   - 🎨 `style: Improve indentation in base template`
   - ✅ `test: Add unit tests for User model`

4. **Special Notes**:
   - If your commit addresses an issue, mention it in parentheses (e.g., `fix: Update form validation (#23)`).
   - Keep changes grouped logically—avoid multiple unrelated changes in one commit.

### 📦 Adding Features and Files
When adding new files, follow these guidelines:

- **HTML Files**: Use clear descriptions. Example: 🚀 `feat: Create contact page template`.
- **Static Files (CSS, JS, images)**:
  - 🎨 `style: Add CSS for navbar`
  - 🔧 `chore: Add JavaScript for form validation`
  - 📦 `build: Update logo in static assets`

### 📥 Pull Requests
1. Ensure your code is thoroughly tested before submitting.
2. Open a PR against the `main` branch, including a clear description.
3. If your PR addresses an issue, mention it (e.g., "Closes #23").
4. 📢 Request a review and make necessary changes based on feedback.

### 🤝 Code of Conduct
Please respect our [Code of Conduct](CODE_OF_CONDUCT.md) to maintain a welcoming environment for all contributors. 

---

Thank you for your contribution! 🌟 Let's work together to make this project better!