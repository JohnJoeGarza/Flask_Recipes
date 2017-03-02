drop table if exists recipes;
create table recipes(
    id integer           primary key autoincrement,
    recipe_name          text not null,
    'recipe_description' text not null
    );