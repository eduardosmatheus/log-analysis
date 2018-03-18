import psycopg2

def get_connection():
    return psycopg2.connect("dbname=news")

def get_most_popular_articles_all_time():
    conn = get_connection()
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
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "select authors.name, count(*) as views from articles inner "
        "join authors on articles.author = authors.id inner join log "
        "on log.path like concat('%', articles.slug, '%') where "
        "log.status like '%200%' group by authors.name order by views desc"
    )
    result = cur.fetchall()
    conn.close()
    return result

def get_one_percent_errors():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "select day, perc from ("
        "select day, round((sum(requests)/(select count(*) from log where "
        "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
        "perc from (select substring(cast(log.time as text), 0, 11) as day, "
        "count(*) as requests from log where status like '%404%' group by day)"
        "as log_percentage group by day order by perc desc) as final_query "
        "where perc >= 1"
    )
    result = cur.fetchall()
    conn.close()
    return result

def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ("\t", results[0], "-", str(results[1]) + "% errors")

if __name__ == "__main__":
    
    most_popular_articles = get_most_popular_articles_all_time()
    print("1. Quais são os três artigos mais populares de todos os tempos?")
    for index, article in enumerate(most_popular_articles):
        title, views = article[0], article[2]
        print("\t", index + 1, "- {title} - {views} views".format(title=title, views=views))
    print("\n")
    
    print("2. Quem são os autores de artigos mais populares de todos os tempos?")
    most_popular_authors = get_most_popular_authors()
    for index, author in enumerate(most_popular_authors):
        author_name, views = author[0], author[1]
        print("\t", index + 1, "- {name} - {views} views".format(name=author_name, views=views))
    
    print("\n")
    print("3. Em quais dias mais de 1% das requisições resultaram em erros?")
    errors = get_one_percent_errors()
    for index, error in enumerate(errors):
        print("\t", index + 1, "- {day} - {average}".format(day=error[0], average=error[1]))



