from database.db.db_connection import get_connection
from models.member.modle import Create_member,Update_member
from fastapi import APIRouter,HTTPException

class Members :
    def create_member(self,body:Create_member):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                query = """INSERT INTO members (name,email,is_activ,total_borrows)
                VALUES (%s,%s,%s,%s)"""
                val = (
                    body.name,
                    body.email,
                    True,
                    0
                )
                try :
                    cursor.execute(query,val)
                    last_id = cursor.lastrowid
                    conn.commit()
                    return last_id
                except :
                    raise HTTPException(status_code=400,detail="This email is already registered in the system.")
    def get_the_members(self):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM members")
                data = cursor.fetchall()
                return data
        
    def get_by_id(self,id:int):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                query="SELECT *FROM members WHERE id = %s"
                cursor.execute(query,(id,))
                data = cursor.fetchone()
                return data
    def patch_member(self,id:int,data:dict):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                parts= []
                val = []
                for key, value in data.items():
                    parts.append(f"{key} = %s")
                    val.append(value)
                val.append(id)
                query = f"UPDATE members SET {", ".join(parts)} WHERE id = %s"
                cursor.execute(query,val)
                conn.commit()
                is_change = cursor.rowcount > 0 
                return is_change

    def disactivate_member(self,id):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                query = "UPDATE members SET is_activ = False WHERE id = %s"
                cursor.execute(query,(id,))
                conn.commit()
                data = cursor.rowcount >0
                return data
    def activate_member(self,id):
        with get_connection() as conn :
            with conn.cursor(dictionary=True) as cursor:
                query = "UPDATE members SET is_activ = True WHERE id = %s"
                cursor.execute(query,(id,))
                conn.commit()
                data = cursor.rowcount >0
                return data
    def get_count_activ_members(self):
         with get_connection() as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT COUNT(*) AS activ_members FROM members WHERE is_activ = True")
                count = cursor.fetchone()
                return count

                    