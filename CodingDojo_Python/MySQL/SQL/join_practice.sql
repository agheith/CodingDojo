/* Find all clients (first and last name) billing amounts and chanrged date. */
/* SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id; */


/* list all of the domain names and leads (first and last name) for each site */
/* SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads on sites.id = leads.sites_id */

/* JOIN ON MULTIPLE TABLES
Get the names of the clietns, their domain names and first names of all the leads generated from those sites. */
SELECT clients.first_name, clients.last_name, sites.domain_name, leads.first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;

/* LEFT & RIGHT JOIN
List all the clients and the sites each client has. even if a client hasnt landed a site yet */

SELECT clients.first_name, clients.last_name, sites.domain_name;
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id;


/* GROUPING ROWS */
SELECT clients.first_name, clients.last_name, SUM(billing.amount)
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;




