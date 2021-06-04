# Comp305 Final Project


## Table of contents
* [General-info](#general-info)
* [Technologies](#technologies)
* [Installation](#Installation)

## General-Info
### Introduction
We are given a list of cities and roads between the cities, as well as a number representing the maximum amount of centers. The goal is to place at most that amount of centers in different cities, such that every city either has a center, or is adjacent to a city with a center. This is a version of the dominating set problem. An optimal solution would have the number of cities with centers equal to the domination number of the graph.
## Technologies
* Python 3

## Installation
``` console
git clone https://github.com/altayatalayy/Comp305.git ./project
cd project
git checkout development
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
## Algorithms
1) Check every option (exponential time) in main.py
  - First parse the graph into an MST, and then check every possible subset of points, to see if they work. The number of subsets of any set is 2^|V|.
  - Time Complexity: exponential in |V|
  - Space Complexity: Linear in |V|


2) Greedy dominating set algorithm in dominating_set_approx.py
  - Greedily choose the vertex with the highest degree, and remove all adjacent vertices from consideration. Repeat until no vertices left. This is an approximation algorithm, but is guaranteed to have no city farther than 1 away from a center.
  - Time Complexity: O( |V|^2 )
  - Space Complexity: Linear in |V|

3) 2-Color Graph Coloring Algorithm (Considered, but not implemented)
  - Model the problem as wanting to color the graph using 2 colors. One color represents the cities with centers, and the other as cities without centers.
  - Time Complexity: A single iteration takes O( |V| ) using breadth-first search, and we can repeat |V| times, each time starting at a new vertex. Then, take the minimum result. The total complexity becomes O( |V|^2 ).
  - Space Complexity: Linear. Just need to store the color of each city, on top of the existing graph.

4) k-Center Algorithm (Considered, but not implemented)
  - Model the problem as having k centers, and wanting to place them in optimal locations. Some cities may be farther than 1 away from a center in the worst case, but if a solution actually exists, no city will be farther than 2 away.
  - Time Complexity: O (k * |V| ) for a single iteration. If ran using all possible variables between k = 1 and k = |V|, we get O ( |V|^3 ) complexity
  - Space Complexity: O ( |V| + |E| ), since we need to store the cities with centers, and also storing the distances between a city and it's nearest center.
