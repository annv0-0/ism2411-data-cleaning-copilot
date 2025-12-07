# Reflection on Copilot use (template)

**What Copilot generated**


- I prepared comments and function signatures that served as prompts for Copilot to generate function bodies.

- Suggested candidate functions: `clean_column_names`, `handle_missing_values`.


**What I modified**


- I reviewed Copilot's suggested code and adjusted column name rules, how numeric conversion errors are handled, and the
  strategy for filling missing values (using median and rounding quantities).


**What I learned**


- Copilot can accelerate routine boilerplate code (e.g., column normalization). However, it may make assumptions about

  data types or missing-value strategies that need careful review. For example, Copilot might fill missing quantities with 0
  but for this dataset median imputation felt more appropriate.


