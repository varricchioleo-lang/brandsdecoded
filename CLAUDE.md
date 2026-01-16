# CLAUDE.md - AI Assistant Guide for brandsdecoded

This document provides essential information for AI assistants working with the brandsdecoded repository.

## Project Overview

**Repository**: brandsdecoded
**Status**: New project (initial setup)

This is the brandsdecoded project repository. This CLAUDE.md file should be updated as the codebase evolves to reflect the current architecture, conventions, and workflows.

## Repository Structure

```
brandsdecoded/
├── CLAUDE.md          # This file - AI assistant guide
└── (additional directories and files to be added)
```

*Update this section as the project structure develops.*

## Development Setup

### Prerequisites

<!-- Update with actual requirements as they are established -->
- Git

### Getting Started

```bash
# Clone the repository
git clone <repository-url>
cd brandsdecoded

# Install dependencies (update with actual commands)
# npm install / pip install -r requirements.txt / etc.
```

## Development Workflow

### Branch Naming Convention

- Feature branches: `feature/<description>`
- Bug fixes: `fix/<description>`
- Documentation: `docs/<description>`
- Claude AI branches: `claude/<session-id>`

### Commit Message Format

Use clear, descriptive commit messages:
- `feat: Add new feature description`
- `fix: Fix bug description`
- `docs: Update documentation`
- `refactor: Refactor component/module`
- `test: Add/update tests`
- `chore: Maintenance tasks`

### Pull Request Process

1. Create a feature branch from main
2. Make changes and commit with descriptive messages
3. Push branch and create pull request
4. Ensure all checks pass
5. Request review and address feedback

## Code Conventions

### General Guidelines

- Write clean, readable, and maintainable code
- Follow the principle of least surprise
- Keep functions/methods focused and single-purpose
- Add comments for complex logic, but prefer self-documenting code
- Handle errors appropriately

### File Organization

- Group related files together
- Use consistent naming conventions
- Keep configuration files at the root level

## Testing

<!-- Update with actual testing instructions -->

```bash
# Run tests (update with actual commands)
# npm test / pytest / etc.
```

### Test Coverage

- Write tests for new features
- Maintain existing test coverage
- Test edge cases and error conditions

## Build and Deployment

<!-- Update with actual build/deploy instructions as established -->

```bash
# Build commands (update as needed)
# npm run build / python setup.py build / etc.

# Deployment (update as needed)
# Deployment process to be documented
```

## Key Files and Entry Points

<!-- Update as the codebase develops -->

| File/Directory | Purpose |
|---------------|---------|
| `CLAUDE.md` | AI assistant guide (this file) |
| `README.md` | Project documentation (to be added) |

## Dependencies

<!-- Track major dependencies here -->

| Dependency | Purpose | Version |
|-----------|---------|---------|
| (none yet) | - | - |

## Common Tasks for AI Assistants

### When Adding New Features

1. Understand the existing codebase structure
2. Follow established patterns and conventions
3. Write tests for new functionality
4. Update documentation as needed
5. Create clear commit messages

### When Fixing Bugs

1. Reproduce the issue first
2. Identify root cause
3. Write a test that fails before the fix
4. Implement the fix
5. Verify the test passes
6. Check for regression impacts

### When Refactoring

1. Ensure tests exist before refactoring
2. Make incremental changes
3. Run tests after each change
4. Maintain backwards compatibility when possible

## Environment Variables

<!-- Document required environment variables -->

| Variable | Description | Required |
|----------|-------------|----------|
| (none yet) | - | - |

## API Documentation

<!-- Add API documentation links/info as developed -->

*API documentation to be added as endpoints are created.*

## Troubleshooting

### Common Issues

<!-- Document common issues and solutions -->

*Add troubleshooting guides as issues are encountered and resolved.*

## Notes for AI Assistants

### Important Considerations

1. **Read before modifying**: Always read and understand existing code before making changes
2. **Preserve patterns**: Follow existing patterns and conventions in the codebase
3. **Minimal changes**: Make focused changes that address the specific task
4. **Security**: Be mindful of security implications in all changes
5. **Testing**: Ensure changes don't break existing functionality

### What to Avoid

- Over-engineering solutions
- Adding unnecessary dependencies
- Making changes outside the scope of the task
- Committing sensitive information (credentials, API keys)
- Breaking existing functionality

---

*Last Updated: January 2026*
*This document should be updated regularly as the project evolves.*
