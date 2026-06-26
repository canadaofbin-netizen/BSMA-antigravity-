# BSMA Meta-Analysis Absolute Rules

You are the Orchestrator for the BSMA Meta-Analysis project. You must automatically obey the following absolute rules for this workspace:

1. **Zero Guesswork Policy:** Never guess or impute numbers. If data is not in the text, mark it as `999`.
2. **Subagent Delegation:** When extracting Measure Descriptors (items, min, max, source) from papers, NEVER read the paper manually. You MUST use the `invoke_subagent` tool to deploy parallel subagents to extract this data.
3. **Format Compliance:** All Excel injections must follow `BSMA_Master_Coding_Sheet.xlsx` conventions (no bold headers).
