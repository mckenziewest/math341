# Math 341 Summary Notes

## Course Logistics

This is a 3 credit 14 week course that meets for 50 minutes 3 times a week.

There are two days during the semester where class will be cancelled for conference and travel purposes.

In Spring 2023, there are 6 students in the course.

The content for this course follows the structure of [Number Theory: In Context and Interactive](https://math.gordon.edu/ntic/) as it is available in 2023. 

## Intended Audience for Course

The prerequisite for Math 341 at the University of Wisconsin-Eau Claire is Calculus 1. 
However, in the semester that these notes are being generated in this manner, all students have taken at least either Linear Algebra or Discrete Math, both of which serve as intro to proof courses at UWEC.
Therefore, there is some assumption as to proof-writing abilities.

## Course Progress Relative to Content
### Introduction (3 days)
* Introduction to Number Theory ... The order of the slides for these days needs updating.
* Materials
    * Slides: [What_Is_NT](Introduction/introduction.slides/What_Is_NT.tex)
    * Worksheet: [day_2](Introduction/day_2.file/day_2.tex) 
    * Worksheet: [day_3](Introduction/day_3.file/day_3.tex).
* Content by Day
  * Day 1: After going through the syllabus, I got through the "Typical questions in Number Theory" content. 
  * Day 2: Worksheet on various famous number theory conjectures.
      * This would be a good opportunity to show students some cool Sage things, like how to list all the primes.
  * Day 3: Prove that 2023 divides one of 11,111,1111,11111,...
      * Note that 2023 can be replaced by anything coprime to 10.

### Chapter 1 (2 days)
* My focus for this chapter is to re-introduce the basics of proof using the tool of divisibility. 
* Materials
    * Slides: [divisibility](Chapter_1/divisibility.slides/divisibility.tex)
    * Worksheet: [Induction_ws](Chapter_1/Induction_ws.file/Induction_ws.tex)
* Content by Day
  * Day 1: Complete content up to induction (hopefully)
  * Day 2: Start with induction examples in slides then pass out worksheet. Again, this worksheet has 3 version so potentially groups could present.

### Chapter 2 (4-5 days)
* Division Algorithm, GCD, Euclidean Algorithm,  Aryabhata's Kuttaka Method
* Materials
    * Python Notebook: [Division_Algorithm_Sage](Chapter_2/div_alg_notebook.file/Division_Algorithm_Sage.ipynb)
    * Slides: [Proofs using division algorithm](Chapter_2/div_alg.slides/div_alg.tex)
    * Slides: [GCD and properties](Chapter_2/gcd.slides/gcd.tex)
    * Slides: [Euclidean Algorithm](Chapter_2/euclidean_algorithm.slides/euclideanalgorithm.tex)
    * Python Notebook: [GCD Facts](Chapter_2/div_alg_notebook.file/Division_Algorithm_Sage.ipynb)
* Content by Day
  * Day 1: Teach students how to generate Sage notebooks and how to use them.
  * Day 2: Complete division algorithm content by proving facts using the division algorithm.
  * Day 3: Define GCD and cover related content, complete associated slides.
  * Day 4: Explain Euclidean Algorithm and how it is used for Aryabhata. (Worksheet)
  * Day 5: Wrap up Chapter with some more gcd facts. Have students prove some properties and add this to the homework.

### Chapter 3 (2 days)
* Solutions to Diophantine Equations
* Materials
    * Slides: [Solving linear Diophantine equations](Chapter_3/diophantine_equations.slides/diophantine_equations.tex)
    * Slides: [Higher diophantine equations](Chapter_3/higher_diophantine.slides/higher_diophantine.tex)
* Content by Day
    * Day 1: Teach students how to use the solution produced by the Kuttaka method to find all solutions to a linear Diophantine equation.
    * Day 2: Finish up any slides not hit in the linear examples, then talk about elliptic curves and Mordell equations for a bit.
    
### Chapter 4 (5 days)
* Congruence
* Materials
    * Slides: [Introduction to Congruence](Chapter_4/congruence.slides/congruence.tex)
    * Slides: [Properties of Congruence](Chapter_4/properties_of_congruence/properties_of_congruence.tex)
    * Slides: [Fast exponentiation](Chapter_4/fast_exponentiation.slides/fast_exponentiation.tex)
    * Notebook:[The basics of congruence equations](Chapter_4/congruence_equations_notebook.file/Congruence_Equations.ipynb)
    
* Content by Day
    * Day 1: Introduce congruence and computing powers mod n
    * Day 2: Prove arithmetic is well-defined
    * Day 3: Prove other properties of congruence 
    * Day 4: Fast exponentiation
    * Day 5: Congruence equations experiments, sums of squares and of cubes

### Chapter 5 (3-4 days)
* Solving systems of congruence equations  
* Materials
  * Slides: [Linear Congruence and CRT](Chapter_5/linear_congruence.slides/linear_congruence.tex)
* Content by Day
  * Day 1: What is a congruence equation, what does it mean to solve a congruence equation, inverses mod $n$
  * Day 2: Basic Chinese Remainder Theorem and lots of examples.
  * Day 3: CRT Extended with non-coprime moduli, equations with coefficients, multiple variables
  
### Chapter 6 (4 days)
* Primes and the Fundamental Theorem of Arithmetic
* Materials
  * Notebook [Prime Exploration](Chapter_6/prime_exploration_notebook.file/prime_exploration.ipynb)
  * Slides [Fundamental Theorem of Arithmetic](Chapter_6/FTA.slides/fund_thm_arithmetic.tex) 
  * (TODO) Slides [Applications of FTA]
* Content by Day
  * Day 1: Students work through the prime exploration notebook. This introduces some prime tools available in Sage.
  * Day 2: Prove the Fundamental Theorem of Arithmetic.
  * Day 3: Proof of infinitely many primes and infinitely many of the form $4k+3$.
  * Day 4: Prime factorizations leading to gcd and lcm, and congruence modulo prime powers.
  
### Chapter 7 (n days)
* Congruence and prime powers
* Materials
  * (TODO) Slides [Hensel's Lemma]
  * (TODO) Notebook [Local Solubility of Polynomials]
  * (TODO) Slides [Wilson's and Fermat's Theorems]