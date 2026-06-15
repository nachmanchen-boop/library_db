# library_db
תיאור המערכת 
מערכת לניהול סיפריה השאלה החזרה הוספה מחיקה חברים בכל 



```
## מבנה תיקיות  
library-api/  
│  
├── app/  
│   ├── main.py  
|   |__logger.py
|   |   
│   ├── database/  
│   │   ├── db\_connection.py  
│   │   ├── book\_db.py  
│   │   └── member\_db.py  
│   ├── routes/  
│   │   ├── book\_routes.py  
│   │   ├── member\_routes.py  
│   │   └── report\_routes.py  
│   └── logs/  
│       └── app.log  
│  
├── README.md  
├── requirements.txt  
└── .gitignore
מבנה הטבלאות 
## books
id PRIMERY KEY AUTO_INCREMENT
title VARCHAR(50) NOT NULL
author VARCHAR(50) NOT NULL
genre ENUM(Fiction | 'Non-Fiction' | 'Science' | 'History' | 'Other') NOT NULL
is_available BOOLEAN NOT NULL
id_member_by_borrowed null | id


## members
id PRIMARY KEY AUTO_INCREMENT
name VARCHAR(50) NOT NULL
email VARCHAR(50) UNIQUE
is_activ BOOLEAN NOT NULL
total_borrows int 

חוקי המערכת 

| חוק | נושא | הכלל |
| ----: | ----: | ----: |
| 1 | יצירת ספר | המשתמש שולח title/author/genre — המערכת מוסיפה `is_available=True`, `borrowed_by=NULL` |
| 2 | genre | חייב להיות Fiction / Non-Fiction / Science / History / Other — כל ערך אחר מחזיר שגיאה יש לוודא הן בהוספה (POST) והן בעדכון (PATCH) |
| 3 | יצירת חבר | המשתמש שולח name/email — המערכת מוסיפה `is_active=True`, `total_borrows=0` |
| 4 | email | חייב להיות ייחודי — אם קיים כבר מחזיר שגיאה |
| 5 | חבר לא פעיל | אם `is_active=False` — אי אפשר להשאיל ספר |
| 6 | ספר לא זמין | אי אפשר להשאיל ספר שכבר מושאל (`is_available=False`) |
| 7 | מקסימום ספרים | חבר לא יכול להחזיק יותר מ-3 ספרים בו-זמנית |
| 8 | החזרת ספר | ניתן להחזיר ספר רק אם הוא מושאל לאותו חבר שמחזיר אותו |

רשימת נקודות קצה
### Books

GET "/books" | יצירת ספר |
GET "/books  | כל הספרים |
GET "/books{id}  |  ספר לפי ID
PATCH "/book/{id}"| עדכון ספר  
PATCH "book/{id}/borrow(member_id)"| השאלת ספר לחבר
PATCH "/books/{id}/return/{member_id}"| החזרת ספר מחבר

## Members
POST "/members" |  יצירת חבר
GET "/members"|  כל החברים
GET "/members{id}"| חבר לפי ID
PATCH "/memners/{id}"| עדכון חבר 
PATCH "/members/{id}/deactivate"| השבתת חבר 
PATCH "/members/{id}/activate| הפעלת חבר 

## Reports

דוח כללי GET "/reports/summary" 
 מספר ספרים כולל  
- מספר ספרים זמינים  
- מספר ספרים מושאלים כרגע  
- מספר חברים פעילים

דוגמה:  
{  
  "total\_books": 0,  
  "available\_books": 0,  
  "currently\_borrowed": 0,  
  "active\_members": 0  
}
ספרים לפי זאנר GET "/reports/books-by-genre"
[  
{"Genre": "Science", "COUNT": 3},  
{"Genre": "History", "COUNT": 2}  
\]

החבר בכי פעיל GET "/reports/top-member
{  
  "member\_id": 1,  
  "borrowed": 5  
}


##זרימת המערכת 
user input 
    |
fast api 
    |
python function
    |
mysql query
    |
response



## Database (Docker)

```bash
docker run --name library_db_mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=library_db -p 3306:3306 -d mysql:8
```

## Run

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.main