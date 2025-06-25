"""
Lab09
Alla pressione del bottone, creare un grafo che rappresenti gli aeroporti collegati da almeno un volo, e distanti in
media almeno x miglia. Il grafo deve essere semplice, non orientato e pesato, i vertici devono rappresentare gli
aeroporti, mentre gli archi devono indicare le rotte tra gli aeroporti collegati tra di loro da almeno un volo. Il peso
dell'arco rappresenta la "distanza media percorsa" tra i due aeroporti, calcolata come la media del campo DISTANCE di
ciascun volo che li collega (poiché il grafo non è orientato, considerare tutti i voli in entrambe le direzioni: A->B
e B->A). L'arco tra due aeroporti deve essere aggiunto solo se la distanza media percorsa è superiore a x.
"""
query = """SELECT T1.ORIGIN_AIRPORT_ID as a1, T1.DESTINATION_AIRPORT_ID as a2,
                  COALESCE(T1.D, 0) + COALESCE(T2.D, 0) as totDistance,
                  COALESCE(T1.N, 0) + COALESCE(T2.N, 0) as nVoli
            FROM
               (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                FROM flights f
                GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T1
            LEFT JOIN
               (SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, SUM(f.DISTANCE) as D, COUNT(*) as N
                FROM flights f
                GROUP BY f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) T2
               ON T1.ORIGIN_AIRPORT_ID = T2.DESTINATION_AIRPORT_ID
                   AND T2.ORIGIN_AIRPORT_ID = T1.DESTINATION_AIRPORT_ID
            WHERE T1.ORIGIN_AIRPORT_ID < T2.ORIGIN_AIRPORT_ID OR
               T2.ORIGIN_AIRPORT_ID IS NULL OR T2.DESTINATION_AIRPORT_ID IS NULL"""

"""
Lab11
Due vertici sono collegati tra loro da un arco, se e solo se nel corso dell'anno a specificato esiste almeno un retailer
che abbia venduto entrambi i prodotti in uno stesso giorno (calcolato tenendo conto delle informazioni contenute in
go_daily_sales). Il peso dell'arco indica il numero di giorni distinti dell'anno a in cui entrambi i prodotti sono stati
venduti da un medesimo retailer.
"""
query = """SELECT p1, p2, count(*) as peso
           FROM (SELECT gds1.Product_number as p1, gds2.Product_number as p2, gds1.`Date` as data
                 FROM go_daily_sales gds1, go_daily_sales gds2
                 where gds1.Retailer_code = gds2.Retailer_code
                           and gds1.`Date` = gds2.`Date`
                           and YEAR(gds1.`Date`)= %s
                           and gds1.Product_number < gds2.Product_number 
                           and gds1.Product_number IN (SELECT gp.Product_number
                                                        FROM go_products gp
                                                        WHERE gp.Product_color = %s)
                           and gds2.Product_number IN (SELECT gp.Product_number
                                                        FROM go_products gp
                                                        WHERE gp.Product_color = %s)
                 GROUP BY p1, p2, data) occorrenze
           GROUP BY p1, p2
           ORDER BY peso desc"""

"""
Lab14
Premendo sul tasto "Crea grafo", l'applicazione costruisce un grafo orientato. I vertici sono gli ordini che sono stati
effettuati nello store selezionato. Gli archi collegano due vertici che sono stati effettuati in un massimo di K giorni.
Il numero massimo di giorni sarà impostato dall'utente tramite l'apposito spazio. Il peso di ogni arco è pari alla
somma degli oggetti comprati nei due ordini collegati.
"""
query = f"""select of1.order_id as source, of2.order_id as target, of1.tot+of2.tot as weight
            from   (select o.order_id as order_id , sum(oi.quantity) as tot, o.order_date as order_date
                    from orders o , order_items oi 
                    where o.order_id = oi.order_id and o.store_id = %s
                    group by o.order_id) of1,
                   (select o1.order_id as order_id , sum(oi1.quantity) as tot, o1.order_date as order_date
                    from orders o1 , order_items oi1 
                    where o1.order_id = oi1.order_id and o1.store_id = %s
                    group by o1.order_id) of2
            where of1.order_id != of2.order_id and of1.order_date > of2.order_date and
            DATEDIFF(of1.order_date, of2.order_date) < %s"""