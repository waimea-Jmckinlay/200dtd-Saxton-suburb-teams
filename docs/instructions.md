# NCEA Level 2 Web and Database Project Instructions



## Introduction

You are required to design and create a web application that satisfies a particular need or problem for a person or group of people. The need / problem should be a genuine and authentic one.

You will be assessed on how skilfully and effectively you design, create, and test your system over the course of a number of 'sprints'

*Note: If you cannot identify a need / problem, [this document](ideas.md) has some that might help you.*

---

## Assessment Standards

| Standard             | Version | Level | Credits |
| -------------------- | ------- | ----- | ------- |
| [91892](as91892.pdf) | 1       | 2     | 4       |
| [91893](as91893.pdf) | 1       | 2     | 4       |


---

## Timeline

You will have 10 weeks to complete this project, broken up into a number of phases:

| Weeks | Phase                                                                       |
| ----- | --------------------------------------------------------------------------- |
| 1     | Project idea clarification, development and research                        |
| 2-3   | **Sprint 1**: DB design and working UI prototype, using DrawSQL and Figma |
| 4-7   | **Sprint 2**: Working MVP (minimum viable product), using Flask template    |
| 8-9   | **Sprint 3**: System refinement and completion                              |
| 10    | Final testing and review                                                |

A 'sprint' is a set period of time during which specific work has to be completed and made ready for review. In this project, the work for each sprint has been defined for you in the table above.

During each sprint you will develop your ideas, create suitable outcomes, present these to your end-user(s) so they can try them out, collect feedback / test data, and improve your outcomes to fix any issues.


---

## Assessment Conditions

This is an 'open book' task. You may look at previous projects that you have worked on, and you may use any notes provided (e.g. the language reference documents).

### Starter Template

A [setup guide](setup.md) and a [project template](template.md) with a minimal Flask application are provided for you. The template has very basic functionality upon which you can build your system.

### Plagiarism and the Use of AI / LLMs

This is an individual assessment activity: Beyond the starter template, all the work that you produce must be your own. Do not copy blocks of code from other people, nor use an AI code-generation tool to write blocks of code for you.

*Note: You will be asked to explain the workings of any/all of your code to assess whether you wrote and understand the code. Also, your git commits will be examined to check how your code progresses.*


---

## What You Need to Hand In

At the end of this project you will need to submit the following:

1. The **URL of your GitHub repo**

2. **A zipped copy** of the repo above

3. **The URL of your live site** - your site must be hosted externally and live for moderation purposes


---

## Achievement Criteria for the Database

Achievement standard [91892](as91892.pdf), Use advanced techniques to develop a database:


| Level          | Criteria                                                     |
| -------------- | ------------------------------------------------------------ |
| **Achieve**    | Use advanced techniques to develop a database.               |
| **Merit**      | Use advanced techniques to develop an **informed** database. |
| **Excellence** | Use advanced techniques to develop an **refined** database.  |

*To help you keep track of how successfully you are meeting the criteria, the items below are in the form of a checklist - mark them off as you work through the project*

### Achieve Criteria

Use advanced techniques to develop a database means that, taking into account the problem / need and the end users:

1. You must first define the purpose of your system and the end-users' needs:
   - [ ] Define the **purpose of the system** that uses the database
   - [ ] Describe the **needs of the end-users**
   - [ ] Define the **key functionality** of the proposed system


2. You need to design the structure of the database:
   - [ ] **Tables** - at least two that are linked by a relationship
   - [ ] **Data Types** - a range of data types used
   - [ ] **Key Fields** - primary keys for each table, foreign keys for relationships
   - [ ] **Values** - auto-generation / default values as required

3. You should use appropriate tools and advanced techniques to organise and query the data:
   - [ ] **Linking data in related tables** using queries or keys
   - [ ] Writing **custom queries** to filter and/or sort data
   - [ ] Using **logical, mathematical and/or wildcard operators** as needed

4. You should use appropriate tools and advanced techniques to present the data:
   - [ ] Customising **presentation** of the data (not just raw data values)
   - [ ] Using **custom forms** to add user input to the database
   - [ ] Setting **validation rules** for data entry

5. You must apply appropriate data integrity and testing procedures:
   - [ ] Show that any **presented data is correct** (e.g. matches database values / calculations)
   - [ ] Show that any input user data **updates the database as expected**

6. You need to explain relevant implications:
   - [ ] Identify the **implications most relevant** to your project
   - [ ] Explain **what the implications mean** and **why each is relevant** to your project
   - [ ] Explain **how each implication will impact your specific project** (considerations / choices / designs)

*Note: You must satisfy **all** of the criteria above to pass*


### Merit Criteria

Use advanced techniques to develop an informed database means **all the criteria for Achieved**, plus:

1. You should use information from testing procedures to improve the quality of your database:
   - [ ] Show **evidence of your testing**, particularly with end-users
   - [ ] Show the **improvements made** as a result

2. You should structure, organise and query your data logically:
   - [ ] Your tables should be **normalised** (no repeating data)
   - [ ] Your fields have the **appropriate data type**, **defaults**, etc.
   - [ ] Your database **queries are well-written and efficient**

3. You must ensure that you have addressed the relevant implications above:
   - [ ] For each one, you need to **explain what you did in your project to address it**


### Excellence Criteria

Use advanced techniques to develop a refined database means **all of the criteria for Merit**, plus:

1. You have made iterative improvements throughout the design, development and testing process:
   - [ ] You have refined features of the DB (the schema and the UI) over **multiple iterations**
   - [ ] Each iteration is **clearly documented**, showing testing and resulting refinements

2. You present the data from the database effectively for the purpose and end users:
   - [ ] Data is displayed in ways that make its **meaning clear** (e.g. using colour)
   - [ ] Data is **displayed in interesting and creative ways** to meet the needs of the user and satisfy the system requirements


---

## Achievement Criteria for the Website (Media Outcome)

Achievement standard [91893](as91893.pdf), Use advanced techniques to develop a digital media outcome:


| Level          | Criteria                                                     |
| -------------- | ------------------------------------------------------------ |
| **Achieve**    | Use advanced techniques to develop a digital media outcome.               |
| **Merit**      | Use advanced techniques to develop an **informed** digital media outcome. |
| **Excellence** | Use advanced techniques to develop an **refined** digital media outcome.  |

*To help you keep track of how successfully you are meeting the criteria, the items below are in the form of a checklist - mark them off as you work through the project*

### Achieve Criteria

Use advanced techniques to develop a digital media outcome means that, taking into account the problem / need and the end users:

1. You must first define the purpose of your system and the end-users' needs:
   - [ ] Define the **purpose of the system** that uses the database
   - [ ] Describe the **needs of the end-users**
   - [ ] Define the **key functionality** of the proposed system

2. You need to use appropriate advanced tools and techniques:
   - [ ] You have used a suitable third-party **web back-end library** (e.g. Flask / Jinja)
   - [ ] You have **written or customised scripts** to implement functionality (e.g. Python)
   - [ ] You have processed data using a **combination of steps** (e.g. data obtained via DB queries, inserted into HTML templates, styled via CSS)

3. You must apply appropriate data integrity and testing procedures:
   - [ ] All webpage text should be checked for **accuracy** (e.g. spell-checked)
   - [ ] Any **data shown is as expected** (i.e. matches database / calculated values)

4. You need to use relevant conventions for a web site:
   - [ ] **Webpage layouts** follow accepted norms
   - [ ] **Data entry forms** follow accepted norms
   - [ ] **Site navigation** follows accepted norms


5. You need to explain relevant implications:
   - [ ] Identify the **implications most relevant** to your project
   - [ ] Explain **what the implications mean** and **why each is relevant** to your project
   - [ ] Explain **how each implication will impact your specific project** (considerations / choices / designs)

*Note: You must satisfy **all** of the criteria above to pass*


### Merit Criteria

Use advanced techniques to develop an informed digital media outcome means **all the criteria for Achieved**, plus:

1. You should use information from testing procedures to improve the quality of your web site:
   - [ ] Show **evidence of your testing**, particularly with end-users
   - [ ] Show the **improvements made** as a result

2. You should apply relevant conventions to improve the quality of the outcome:
   - [ ] Your web site works on a **variety of screen sizes** (as appropriate)
   - [ ] You have **addressed accessibility** through the use of semantic tags, image alt text, etc.
   - [ ] **Navigation is easy to use** throughout the site

3. You must ensure that you have addressed the relevant implications above:
   - [ ] For each one, you need to **explain what you did in your project to address it**


### Excellence Criteria

Use advanced techniques to develop a refined digital media outcome means **all of the criteria for Merit**, plus:

1. You have made iterative improvements throughout the design, development and testing process:
   - [ ] You have refined features of the web site (layout, theme, etc.) over **multiple iterations**
   - [ ] Each iteration is **clearly documented**, showing testing and resulting refinements

2. You have used efficient tools and techniques in the web site's production:
   - [ ] Your project **assets are managed well** (file naming, appropriate folders, etc.)
   - [ ] You have used your own **stylesheets** to customise the look of the site
   - [ ] You have made good use of **templates** (Jinja) to organise and structure content
   - [ ] Your code is **commented** as needed
   - [ ] Any generated **HTML has been validated**
   - [ ] Your **CSS has been validated**
   - [ ] You have **optimised media assets** (e.g. image sizing)


