
## Why should I care?  
%%Touch on origin story%%
%%Say this has been a focus for you%%
Pragmatic Programming is focused on delivering quality code.
1. Clients happy
2. Coworkers happy
3. BAH reputation
4. Off and on boarding easy 
5. Keep YOU happy (all hair remains on head)

---

## Why should I care?  
Programming is to data science as singing and playing guitar are to songwriting.
You might have some great ideas, but you're going to have trouble validating and selling them if you struggle with programming.

---
## Data Scientists and Programming
%%These are software engineering principles but they carry over to data science%%
%%If you are a quality engineer you can really differentiate yourself here%%
- Dashboards
- Models and Simulation
- Optimization
- Cloud Infrastructure
*It's all built upon code*

### The Evils of Duplication
[[TPP#7.-The Evils of Duplication]]
*Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.*
%%QUESTION: 
Has anyone ever made a simple change to the code but needed to change it like 100 times throughout the codebase??
you may not be DRY
%%
**Tip 11: DRY—Don't Repeat Yourself**
%%Sources of duplication:
-   **Imposed duplication** Developers feel they have no choice—the environment seems to require duplication.
-   **Inadvertent duplication** Developers don't realize that they are duplicating information.
-   **Impatient duplication** Developers get lazy and duplicate because it seems easier.
-   **Interdeveloper duplication** Multiple people on a team (or on different teams) duplicate a piece of information.%%

*Make your code easy to reuse*
%%
Q: How might we make our code easy to reuse?
1. Document it
2. Publicize it
3. Review each other's code
4. Make it modular (single responsibility principle)
%%

%%
CODE EXAMPLE
The developer id for your spotify account
%%


---
### Orthogonality / Decoupling
[[TPP#Orthogonality]]
[[TPP#26.-Decoupling and the Law of Demeter]]
[[SOLID#Single Responsibility Principle]]
![[orthogonal-vector-271x300.jpg]]
-   Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
-   Each unit should only talk to its friends; don't talk to strangers.
-   Only talk to your immediate friends.
%%EXAMPLE
UI combines modeling code and feature engineering code in one big ole function
%%
%%Show an imaginary email from the boss looking to try new models%%
%%Hilarity ensues%%

---
### Decoupling and the Law of Demeter
%%QUESTION: Has anyone ever been afraid to change code because they aren't sure what else my be effected by their change?%%
%%Or have you seen one simple change break something unrelated way accross your program?%%
[[TPP#26.-Decoupling and the Law of Demeter]]
[[SOLID#Dependency Inversion Principle]]



%%
CODE EXAMPLE
Have a feature engineering function that changes the name of a column in the dataframe

then show an email that shows the function needed to be removed
then show that the column was directly referenced in the model code
and the program breaks.
%%


---
### Program By Coincidence  
[[TPP#31.-Program by Coincidence]]
[TDS - Unit Testing for Data Scientists](https://towardsdatascience.com/unit-testing-for-data-scientists-dc5e0cd397fb)
Don't  
*Walk through bit by bit of what people might do*
confirm your assumptions
%%come up with a good pandas example%%  

---

[[TPP#]]
Include don't outrun your headlights

---
## Tracer Bullets
%%In new projects your users requirements may be vague. Use of new algorithms, techniques, languages, or libraries unknowns will come. And environment will change over time before you are done. We're looking for something that gets us from a requirement to some aspect of the final system quickly, visibly, and repeatably.%%

%%TODO: Show the hill picture%%
%%OR a Picture of a code skeleton%%

**Tip 15: Use Tracer Bullets to Find the Target**

Advantages:

-   Users get to see something working early
-   Developers build a structure to work in
-   You have an integration platform
-   You have something to demonstrate
-   You have a better feel for progress


### Tracer Bullets Don't Always Hit Their Target

Tracer bullets show what you're hitting. This may not always be the target. You then adjust your aim until they're on target. That's the point.

---
### Debugging  
- Know your tools
DEBUG PICTURE
%%Insert image of book?%%
- [Debugging: The 9 Indespensable Rules](https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814474578)
	- [Free Summary](https://inspirezone.tech/9-indispensable-rules-for-debugging-software-and-hardware/)


---
### Algorithm Speed  
#### Profiling (Performance)  
CProfile  

---
### Pragmatic Teams  
- No Broken Windows  
- black?  
- Boiled Frogs  
- Communicate  
Link smart Brevity  
- DRY  
- Orthogonality  
---
### Refactoring
[[TPP#33.-Refactoring]]
- don't build a bridge, cultivate a garden.  


%%
Code needs to evolve; it's not a static thing.

### When Should You Refactor?

-   Duplication. You've discovered a violation of the DRY principle
-   Nonorthogonal design. You've discovered some code or design that could be made more orthogonal 
-   Outdated knowledge. Things change, requirements drift, and your knowledge of the problem increases. Code needs to keep up.
-   Performance. You need to move functionality from one area of the system to another to improve performance.

**Tip 47: Refactor Early, Refactor Often**

### How Do You Refactor?

-   1.  Don't try to refactor and add functionality at the same time.
-   2.  Make sure you have good tests before you begin refactoring.
-   3.  Take short, deliberate steps.
%%
---
### Ubiquitous Automation  
black?  
pre-commit?  
isort?  
sphinx



---
# ARCHIVE


---
## Why Should I Care?

When Data Scientists **ignore** programming principles they are more likely to:
1. make mistakes %%You need to know what your code does!%%
2) miss deadlines  %%90 percent of your dev time will be spent doing non-DS stuff%%
3) experience stress %%Diving back to a mistake you made months ago%%

Data Scientists who **embrace** programming principles deliver projects with greater:
1) maintainability %%You can make future changes faster%%
2) reliability %%your code is more likely to do what you say it does. It will also be clear to other DS what your code does%%
3) learnability %%If you get promoted, moved to another project, expand the team. Your code can be used by someone else!%%


---
### Decoupling - Example
![[Pasted image 20230622160221.png]]



---
### Decoupling - Example
![[Pasted image 20230622163110.png]]

---
### Decoupling - Example

![[highline.png]]

---
### Decoupling - Story
![[Pasted image 20230623212618.png]]

---
### Software Entropy and Broken Windows
%%This anecdote reflects my views on software, NOT LAW ENFORCEMENT%%
>One **broken window**, instills in the inhabitants of the building a sense of abandonment—a sense that the powers that be don't care about the building. So another window gets broken. People start littering. Serious structural damage begins. the building becomes damaged beyond the owner's desire to fix it, and the sense of abandonment becomes reality.