import database

def get_most_popular_articles_all_time():
    conn = database.get_connection()
    cur = conn.cursor()
    cur.execute(
        "select articles.title, log.path, count(*) as views "
        "from articles "
        "inner join log on log.path like concat('%', articles.slug, '%') "
        "where log.status like '%200%' "
        "group by articles.title, log.path "
        "order by views desc limit 3"
    )
    result = cur.fetchall()
    conn.close()
    return result
    

def get_most_popular_authors():
    conn = database.get_connection()
    cur = conn.cursor()
    cur.execute(
        ""
    )
    result = cur.fetchall()
    conn.close()
    return result
    



