def enrollment_create(db, data):
    print("CREATE > ", data)
    with db.session() as session:
        # session.run("CREATE (a:Enrollment {studentId: $studentId})", studentId = data['studentId'])
        session.run(
            "MERGE (s:Student {studentId: $studentId}) " +
            "MERGE (c:Course {courseNum: $courseNum}) " +
            "MERGE (s)-[r:Enrolled]->(c)", studentId = data["studentId"], courseNum = data["courseNum"])

def enrollment_delete(db, data):
    print("DELETE > ", data)
    with db.session() as session:
        # session.run("MATCH (a: Enrollment {studentId: $studentId}) DETACH DELETE a", studentId = data['studentId'])
        session.run(
            "MATCH (s:Student {studentId: $studentId})-[r:Enrolled]->(c:Course {courseNum: $courseNum}) " +
            "DELETE r", studentId = data["studentId"], courseNum = data["courseNum"])

# "MATCH (s1:Student {studentId: $studentId})-[r:Enrolled]->(c1:Course)<-[r2:Enrolled]-(s2:Student)-[r3:Enrolled]->(c3:Course) " +
# "RETURN c3"