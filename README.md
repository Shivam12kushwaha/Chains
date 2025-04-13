# Chains
#### Chain components are essential in building blocks that allows you to create multi-step workflows by linking different LLMs calls,tools, and functions together.
## (1) Simple Chain:
####   In LangChain, a Simple Chain is a basic construct that connects one or more components together typically a prompt template, a LLM, and optionally a parser or output processor.
## (2) Sequential Chain:
####   A Sequential Chain in LangChain is a type of chain where multiple steps (or links) are executed one after another, and each step's output becomes the next step's input.
###    Types of Sequential Chains:
####   (a) *SimpleSequentialChain* Passes only the final output from one step to the next (like chaining functions).
####   (b) *SequentialChain* Passes a dictionary of inputs and outputs, allowing access to all intermediate results.
## (3) Parellel Chain:
####   A Parallel Chain (often implemented as a MultiPromptChain or custom logic) runs multiple chains at the same time, and then collects or compares the results.
###    "One input → Multiple chains run in parallel → Multiple outputs"
###    When to Use Parallel Chains:
####   Content generation with multiple styles or tones
####   Ensemble reasoning (e.g., getting multiple viewpoints)
####   Running different models (e.g., Claude, GPT-4, Mistral) for comparison
####   Decision making
## (4) Conditional Chain:
####   In LangChain, a Conditional Chain is a type of chain that routes the input to different sub-chains based on some condition or logic.
