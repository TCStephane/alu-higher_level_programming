# SQL - More Queries

A collection of SQL scripts covering advanced MySQL concepts — users, privileges, constraints, joins, and subqueries — as part of the ALU Higher Level Programming curriculum.

## Learning Objectives

By the end of this project, you should be able to explain:

- How to create a new MySQL user and manage privileges
- What PRIMARY KEY and FOREIGN KEY are
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables using JOIN
- What subqueries are and how to use them
- What UNION is and how to use it

## Requirements

- MySQL 8.0 (Ubuntu 20.04 LTS)
- All SQL keywords must be uppercase
- Every query must have a comment just before it
- Every file must start with a comment describing the task

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-privileges.sql` | List privileges of user_0d_1 and user_0d_2 |
| 1 | `1-create_user.sql` | Create user_0d_1 with all privileges |
| 2 | `2-create_read_user.sql` | Create database and user with SELECT only |
| 3 | `3-force_name.sql` | Create table with NOT NULL name |
| 4 | `4-never_empty.sql` | Create table with default id value |
| 5 | `5-unique_id.sql` | Create table with unique id |
| 6 | `6-states.sql` | Create states table with PRIMARY KEY |
| 7 | `7-cities.sql` | Create cities table with FOREIGN KEY |
| 8 | `8-cities_of_california_subquery.sql` | List California cities using subquery |
| 9 | `9-cities_by_state_join.sql` | List all cities with state name using JOIN |
| 10 | `10-genre_id_by_show.sql` | List shows with at least one genre |
| 11 | `11-genre_id_all_shows.sql` | List all shows with genre, NULL if none |
| 12 | `12-no_genre.sql` | List shows without a genre |
| 13 | `13-count_shows_by_genre.sql` | Count shows per genre |
| 14 | `14-my_genres.sql` | List genres of Dexter |
| 15 | `15-comedy_only.sql` | List all Comedy shows |
| 16 | `16-shows_by_genre.sql` | List all shows and their genres |

## Author

Stephane Tchatchum — African Leadership University, Kigali
