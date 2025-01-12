# Frontend Code Review Guidelines

## Purpose
This document outlines the code review process and requirements for the frontend team. Following these guidelines ensures consistent, high-quality code reviews that facilitate knowledge sharing and maintain code quality.

## 1. Context Requirements

Every feature merge request must include a Business Requirements Document (BRD). This document helps reviewers understand the purpose and scope of the changes.

Including proper context reduces review time and helps catch potential issues early in the development cycle.

## 2. Test Plan

A comprehensive test plan demonstrates that your code works as intended and provides a reference for future maintenance.

### Required Components

**Visual Documentation**
- Include screenshots or GIFs showing the feature in action
- Capture both successful flows and error states
- Keep videos focused and under 30 seconds

**Test Scenarios**
- Document the testing environment and prerequisites
- List manual test cases with clear steps
- Include edge cases and error conditions

A good test plan serves as a trust token between team members and becomes valuable documentation for future reference.

## 3. Pull Request Size and Focus

Follow the "One diff, one thesis" principle by keeping pull requests focused and manageable.

### Size Guidelines
- Target size: 50-250 lines of code
- Maximum recommended size: 250 lines
- Larger changes should be split into smaller, logical chunks

### Breaking Down Large Changes
When a feature requires extensive changes, break it down into smaller PRs following a logical sequence:
1. foundational changes (New files, new UI components)
2. Core functionality
3. Feature enhancements and polish

## 4. Code Quality Standards

All code submissions should meet the following quality standards:

**Technical Requirements**
- Follow established coding style and patterns (Consistency, avoid unecessary overengineering (KISS), remove unused variables, use pure functions, use descriptive and meaningful variable names)
- Ensure proper error handling
- Consider performance implications
- Maintain accessibility standards

**Documentation**
- Update component documentation
- Add inline comments for complex logic

## 5. Review Process

### Timeline Expectations
- Initial review: Within 1 business day
- Follow-up reviews: Within 4 business hours
- Critical fixes: Same day review

### Review Focus Areas
- Functionality: Does it work as intended?
- Code quality: Is it maintainable and efficient?
- Testing: Is it properly tested?
- Documentation: Is it well documented?

## Best Practices

1. **Early Feedback**
   Start code reviews early by creating draft PRs for discussion of approach and architecture.

2. **Clear Communication**
   Use clear and constructive language in review comments. Focus on the code, not the developer.

3. **Iterative Improvement**
   Address feedback promptly and keep the review cycle moving forward.

4. **Knowledge Sharing**
   Use code reviews as an opportunity to share knowledge and mentor team members.