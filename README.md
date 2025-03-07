Documented and Refactored Changes:


## Technical Debt Identified
- Poor naming convention
- Lacking module functions
- Hardcoded values instead of dynamic inputs
- No error handling
- Code duplication


## Refactoring Improvements  
- Improved variable & function naming  
- Used constants for clarity  
- Enhanced formatting with f-strings  
- Added comments & error handling
- Scalability adding and deduction is easier
- Code is easier to debug and update
- Code logic is broken down to smaller portions
- Reasuable functions within the code


## Challenges Faced & Solutions  

| **Challenges** | **Solutions Implemented** |  
|--------------|------------------------|  
| **Ensuring accuracy of deductions** | Replaced hardcoded values with **dynamic calculations** (e.g., SSS based on salary brackets, Pag-IBIG capped at ₱100, and progressive tax system). |  
| **Handling invalid user inputs** | Added **error handling** to catch non-numeric or negative salary inputs using a `try-except` block. |  
| **Improving readability and maintainability** | Used **descriptive variable names, constants, and modular functions** to make the code more understandable. |  
| **Reducing code duplication** | Separated deduction calculations into **reusable functions** to avoid repeating logic. |  
| **Enhancing output formatting** | Used **f-strings and aligned text formatting** to improve the readability of the salary breakdown. |  
| **Scalability for future tax/deduction updates** | Structured the code to allow **easy modification of rates and policies** without changing multiple parts of the code. |  


Members:
Ian Reister Baragona - Project Manager
Jin Caleb Bicar - Lead Developer
Gabriel Luke Tocle - Git Manager
Jon Paolo Dimarucut - Refactoring Specialist
