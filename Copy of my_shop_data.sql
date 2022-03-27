Select employee.employee_id, sum(orders.unitprice*orders.quantity) as sold
from employee
left join orders
on employee.employee_id = orders.employee_id
group by employee.employee_id
order by sold desc; 

select customers.customer_id, sum(orders.unitprice*orders.quantity) as sold
from customers
left join orders
on customers.customer_id = orders.customer_id
group by customers.customer_id
order by sold desc;

select productname, sum(orders.unitprice*orders.quantity) as sold
from products
left join orders
on products.product_id = orders.product_id
group by productname
order by sold desc;

select productname, sum(orders.unitprice*orders.quantity) as sold, products.type1
from products
left join orders
on products.product_id = orders.product_id
group by productname, products.type1
order by sold desc;

