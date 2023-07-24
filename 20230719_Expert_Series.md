
## Pragmatic Programming for Data Scientists
*Tips to deliver better analytics solutions faster*
![[book_cover.jpg]]


---
## Disclaimers
1. Speak up! %%These are not secrets. Everyone knows this stuff and has valuable perspective. I don't need to finish all my slides%%
	- We do **NOT** need to finish my slides
2. Think about your own projects
	- data scientists write code
	- managers review code
	- business analysts request code
	%%This helps anyone who writes code write it better. but its also good for managers to encourage their underlings to read up. and have a shared language around code quality%%
3. Dive deeper %%Or some equivalent, if you want the full picture%%

---
## Why Should I Care?
As a data scientist you might have great ideas. If you can't implement them reliably in your code, they will never make an impact!
 ![Code Quality](artifacts/code_quality_graph.png.png)
%%We don't typically have the luxury of dedicated software engineers on our projects, we're working on client facing solutions%%

---
### The Essence of Good Design

>Good design is easier to change than bad design

%%this is the whole purpose of the presentation%%

---
### Principles of Good Design
- Data Scientists can deliver more value to clients by embracing pragmatic programming principles!
	1. Don't Repeat Yourself (DRY)
	2. Metaprogramming
	3. Decoupling
*\*not comprehensive*
---
### Don't Repeat Yourself (DRY)
*Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.*
%%QUESTION: 
Has anyone ever made a simple change to the code but needed to change it like 100 times throughout the codebase??
you may not be DRY
%%

---
### DRY Example
%%See Notebook%%
[Notebook Link](https://github.com/PatrickBrayPersonal/spotify-playlists/blob/main/notebooks/dry_example.ipynb)

---
### Metaprogramming

**Dependency Inversion Principle**
>Details should depend on abstractions, abstractions should not depend on details

---
### Metaprogramming in Data Science
- Data Science pieces to put into config files / command line
	1) Column names
	2) Parameters
	3) Test vs Prod
	4) Database connections

---
### Metaprogramming Example
%%See notebook%%
[Notebook Link](https://github.com/PatrickBrayPersonal/spotify-playlists/blob/main/notebooks/dry_example.ipynb)


---
### Decoupling

*Separation of Concerns*
- No rube-goldberg machines!
- Have **changable**, **independent** parts with contracts for communication

---
### Decoupling Actions
1. Change your **monolith** jupyter notebook to a **modular** python codebase
2. **Separate** your ML code, data transformations, and database connections into different modules

### Decoupling Benefits
1. New teammates can work on single parts without understanding the whole codebase
2. People feel free to change code knowing it won't break other workflows


---
## Coupled or Decoupled
![[potatohead.jpg]]

---
## Coupled or Decoupled
![[mousetrap.png]]

---

## Coupled or Decoupled

![[s-l1600.jpg]]
---
## Coupled or Decoupled

![[Macbook.jpeg]]


---
### Warning - Software Entropy
%%*AKA: Technical Debt*, AKA: Code Rot%%
%%Has anyone ever looked at a codebase and felt like they're looking at something like this?%%
%%This is something that happens naturally as time progresses%%
%%This might have been organized once upon a time but then one operator adds one wire, then the next adds two, then a new hire is asked to make changes and they see its messy. So they think that's the norm%%


%%Design is not a one time thing%%
%%You are not building a bridge, you are cultivating a garden%%
%%Bridges are rigid, gardens are constantly changing%%
<html>
<img src="artifacts/wires.jpg"  width="600" height="300">
</html>
![Wires](artifacts/wires.jpg)

%%[[TPP#2.-Software Entropy]]
[[TPP#33.-Refactoring]]%%
%%An ounce of prevention is worth a pound of cure%%

---
### What Now?
1. Read (see *References*)
	- This presentation is just the tip of the iceberg
2. Explore (see *Recommended Tools*)
	- Many libraries make effective program design easier
3. Discuss
	- Talk through with your team how you might improve your program design
	- Establish a shared language

---
## Thank you for coming to my TED talk
### Concepts Covered
1. Don't Repeat Yourself (DRY)
2. Metaprogramming
3. Decoupling

>Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it. - Kernhigan's Law

%%This is just the tip of the Icebe%%

---
## Template Repository
https://github.boozallencsn.com/Bray-Patrick/dsms-ml-template

---
## Recommended Tools
*All python, all open source*

#### Machine Learning
- [hydra](https://hydra.cc/docs/intro/#introduction)
	- Config and experimentation orchestration
	- [Intro Article](https://medium.com/pytorch/hydra-a-fresh-look-at-configuration-for-machine-learning-projects-50583186b710)
	- Lightweight alternative: [Python Fire](https://google.github.io/python-fire/guide/)
- [mlflow](https://mlflow.org/docs/latest/what-is-mlflow.html)
	- Experiment tracking and model versioning
	- Subscription-based alternative:  [Weights & Biases](https://wandb.ai/site)
#### Documentation
- [pdoc](https://pdoc.dev/docs/pdoc.html#customizing-pdoc)
	- Automatically builds API documentation
		- see the example docs [here](https://pages.github.boozallencsn.com/Bray-Patrick/dsms-ml-template/your_package.html)
	- More configurable alternative: [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
- [ghp-import](https://pypi.org/project/ghp-import/)
	- Lightweight GitHub pages for documentation automation
	- Heavier and more automated alternative: [Github Actions](https://github.com/features/actions)
#### Formatting (PEP8)
- [black](https://pypi.org/project/black/)
	- automatically format code
- [isort](https://pycqa.github.io/isort/)
	- automatically sort imports
- [flake8](https://flake8.pycqa.org/en/2.5.5/config.html)
	- find linting issues not fixed by black
#### Other
- [invoke](https://www.pyinvoke.org/)
	- manage command line workflows using python
	- OS agnostic, unlike Makefile
- [pytest](https://docs.pytest.org/en/7.3.x/)
	- python test management framework
	- More configurable alternative: [unittest](https://docs.python.org/3/library/unittest.html)
- [poetry](https://python-poetry.org/)
	- Dependency and environment management
	- Classic alternative: [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [theskumar/python-dotenv](https://github.com/theskumar/python-dotenv)
	- automatically read and access environment variables
- [loguru](https://loguru.readthedocs.io/en/stable/overview.html#)
	- easy logging, better api
- [cProfile](https://docs.csc.fi/computing/cProfile/)
	- measure what is slowing your code  
- [dotenv](https://github.com/theskumar/python-dotenv)
	- Load environment variables easily  

### IDE Tools
- [VSCode Debugger](https://code.visualstudio.com/docs/editor/debugging)
- [VSCode Test Explorer UI](https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer)

---

## References

### Books
- [The Pragmatic Programmer](https://www.amazon.com/Pragmatic-Programmer-journey-mastery-Anniversary/dp/0135957052)
	- [Free Summary](https://github.com/HugoMatilla/The-Pragmatic-Programmer)
- [Pragmatic Programmer for ML](https://www.taylorfrancis.com/books/mono/10.1201/9780429292835/pragmatic-programmer-machine-learning-marco-scutari-mauro-malvestio)
- [Debugging: The 9 Indespensable Rules](https://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814474578)
	- [Free Summary](https://inspirezone.tech/9-indispensable-rules-for-debugging-software-and-hardware/)
- [Designing Machine Learning Systems](https://learning.oreilly.com/library/view/designing-machine-learning/9781098107956/)

### Articles 
- [SOLID Principles Python](https://realpython.com/solid-principles-python/)
- [Write decoupled code — Good research code](https://goodresearch.dev/decoupled.html)
- [Separation of Concerns: the Simple Way](https://dev.to/tamerlang/separation-of-concerns-the-simple-way-4jp2)

### YouTube
- [Scaling ML Adoption: Pragmatic Approach](https://www.youtube.com/watch?v=AUvAdkDvvto)  
- [How Principled Coders Outperform the Competition](https://www.youtube.com/watch?v=q1qKv5TBaOA])

