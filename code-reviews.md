Code review framework for frontend team.

1. Context

Feature MRs must have a BRD attached to it. this helps the reviewer to gather knowledge about what the code review is trying to achieve.

2. Test plan

A test plan is used to show that your code actually works.

It should be visual if possible. it can be a list of all the test cases and steps to verify those test cases. this could take time so its best to use video or a gif.

Example of a test plan
https://github.com/Gear61/Random-Name-Picker/pull/183

Benefits of having a test plan:

- Basic trust token showing your teammates that your code works, at least in the core flow
- Turns your code review into a much more informative and self-documented piece of codebase history
- Makes it far easier for people not to break whatever is in your code review when they work with it in the future

Show a repeatable way to test your change

- If you're adding automated tests, include the command to run it
- With a video, show the full process of triggering the flow altered by the commit (e.g. tapping into a certain screen on a website)


3. Create small and focused PRs follow the "One diff, one thesis" principle

Every commit and pull request (PR) you put out should have a singular focus. Don't just dump your entire feature into 1 massive 2,500 line PR; it's extremely difficult to review and you are robbing yourself of real technical feedback.
A good average range for a PR is 50-250 lines of code. If it's substantially higher than 250, there's a good chance your PR is simply too big.

Breaking up your pull requests will take more time initially (10-15 minutes), but it's completely worth it as it saves you time in the long-term. Smaller, more focused PRs get better feedback and are merged in faster.

Having this habit alongside all the other good code review behaviors (linked below) is one of the most straightforward way to get a stellar performance review as an earlier-in-career engineer. Conversely, not following these guidelines is one of the easiest ways to have bad performance as a software engineer.