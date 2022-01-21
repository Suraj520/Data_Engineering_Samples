--1. Cut off 30% tax on all employees whose salary is greater than 60000, 20% for all those whose salary is between 30,000 to 60,000 and none if less than 30,000 INR. Display the net salary in a new COLUMN
 SELECT sal.emp_no,sal.salary, sal.from_date, sal.to_date, 
    CASE WHEN sal.salary > 60000
    THEN round(sal.salary*0.2)
    WHEN sal.salary > 60000 AND sal.salary > 30000
    THEN round(sal.salary*0.2)
    ELSE sal.salary
    END AS NET_SALARY
    FROM salaries sal
