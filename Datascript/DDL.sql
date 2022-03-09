create table Matter(
    MATTER_ID   SERIAL not null,
    SEMESTER INTEGER not null,
    NAME VARCHAR(50) not null,
    CODE VARCHAR(7) not null,
    TEACHER VARCHAR(50) not null,
    description VARCHAR(100) null,
    color_hex VARCHAR(8) not null,
    page VARCHAR(50) null,
    constraint PK_MATTER primary key (MATTER_ID)
)