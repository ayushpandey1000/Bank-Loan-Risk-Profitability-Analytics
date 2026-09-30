-- ============================================================
-- BANK LOAN RISK & PROFITABILITY ANALYTICS
-- SQL Analysis
-- ============================================================

USE bank_loan_analytics;


-- ============================================================
-- 1. OVERALL PORTFOLIO METRICS
-- ============================================================

SELECT
    COUNT(*) AS total_loans,
    SUM(loan_amnt) AS total_loan_amount,
    AVG(loan_amnt) AS average_loan_amount,
    SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END) AS total_defaults,
    ROUND(
        100.0 * SUM(CASE WHEN `Default` = 1 THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS default_rate
FROM loan_data;


-- ============================================================
-- 2. DEFAULT RATE BY FICO SCORE
-- ============================================================

SELECT
    CASE
        WHEN fico_n < 650 THEN 'Below 650'
        WHEN fico_n < 700 THEN '650-699'
        WHEN fico_n < 750 THEN '700-749'
        ELSE '750+'
    END AS fico_band,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate

FROM loan_data

GROUP BY
    CASE
        WHEN fico_n < 650 THEN 'Below 650'
        WHEN fico_n < 700 THEN '650-699'
        WHEN fico_n < 750 THEN '700-749'
        ELSE '750+'
    END

ORDER BY default_rate DESC;


-- ============================================================
-- 3. DEFAULT RATE BY DTI
-- ============================================================

SELECT
    CASE
        WHEN dti_n < 10 THEN '0-10'
        WHEN dti_n < 20 THEN '10-20'
        WHEN dti_n < 30 THEN '20-30'
        WHEN dti_n < 40 THEN '30-40'
        ELSE '40+'
    END AS dti_band,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate

FROM loan_data

WHERE dti_n IS NOT NULL

GROUP BY
    CASE
        WHEN dti_n < 10 THEN '0-10'
        WHEN dti_n < 20 THEN '10-20'
        WHEN dti_n < 30 THEN '20-30'
        WHEN dti_n < 40 THEN '30-40'
        ELSE '40+'
    END

ORDER BY default_rate DESC;


-- ============================================================
-- 4. DEFAULT RATE BY LOAN AMOUNT
-- ============================================================

SELECT
    CASE
        WHEN loan_amnt < 5000 THEN '0-5K'
        WHEN loan_amnt < 10000 THEN '5K-10K'
        WHEN loan_amnt < 20000 THEN '10K-20K'
        WHEN loan_amnt < 30000 THEN '20K-30K'
        ELSE '30K-40K'
    END AS loan_amount_band,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate

FROM loan_data

GROUP BY
    CASE
        WHEN loan_amnt < 5000 THEN '0-5K'
        WHEN loan_amnt < 10000 THEN '5K-10K'
        WHEN loan_amnt < 20000 THEN '10K-20K'
        WHEN loan_amnt < 30000 THEN '20K-30K'
        ELSE '30K-40K'
    END

ORDER BY default_rate DESC;


-- ============================================================
-- 5. DEFAULT RATE BY ANNUAL INCOME
-- ============================================================

SELECT
    CASE
        WHEN revenue < 40000 THEN 'Below 40K'
        WHEN revenue < 60000 THEN '40K-60K'
        WHEN revenue < 90000 THEN '60K-90K'
        WHEN revenue < 150000 THEN '90K-150K'
        ELSE '150K+'
    END AS income_band,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate

FROM loan_data

GROUP BY
    CASE
        WHEN revenue < 40000 THEN 'Below 40K'
        WHEN revenue < 60000 THEN '40K-60K'
        WHEN revenue < 90000 THEN '60K-90K'
        WHEN revenue < 150000 THEN '90K-150K'
        ELSE '150K+'
    END

ORDER BY default_rate DESC;


-- ============================================================
-- 6. DEFAULT RATE BY LOAN PURPOSE
-- ============================================================

SELECT
    purpose,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate

FROM loan_data

GROUP BY purpose

ORDER BY default_rate DESC;


-- ============================================================
-- 7. STATE-WISE DEFAULT RATE
-- Only states with at least 5,000 loans
-- ============================================================

SELECT
    addr_state,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate

FROM loan_data

GROUP BY addr_state

HAVING COUNT(*) >= 5000

ORDER BY default_rate DESC;


-- ============================================================
-- 8. RISK SEGMENTATION
-- ============================================================

SELECT
    CASE
        WHEN fico_n < 650 AND dti_n >= 30
            THEN 'Very High Risk'

        WHEN fico_n < 700 AND dti_n >= 30
            THEN 'High Risk'

        WHEN fico_n < 700 OR dti_n >= 30
            THEN 'Moderate Risk'

        ELSE 'Lower Risk'
    END AS risk_segment,

    COUNT(*) AS total_loans,

    SUM(
        CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
    ) AS defaults,

    ROUND(
        100.0 * SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS default_rate,

    ROUND(
        AVG(loan_amnt),
        2
    ) AS avg_loan_amount

FROM loan_data

WHERE dti_n IS NOT NULL

GROUP BY
    CASE
        WHEN fico_n < 650 AND dti_n >= 30
            THEN 'Very High Risk'

        WHEN fico_n < 700 AND dti_n >= 30
            THEN 'High Risk'

        WHEN fico_n < 700 OR dti_n >= 30
            THEN 'Moderate Risk'

        ELSE 'Lower Risk'
    END

ORDER BY default_rate DESC;


-- ============================================================
-- 9. STATE RISK RANKING
-- CTE + DENSE_RANK WINDOW FUNCTION
-- ============================================================

WITH state_risk AS (

    SELECT
        addr_state,

        COUNT(*) AS total_loans,

        SUM(
            CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
        ) AS defaults,

        ROUND(
            100.0 * SUM(
                CASE WHEN `Default` = 1 THEN 1 ELSE 0 END
            ) / COUNT(*),
            2
        ) AS default_rate

    FROM loan_data

    GROUP BY addr_state

    HAVING COUNT(*) >= 5000
)

SELECT
    addr_state,
    total_loans,
    defaults,
    default_rate,

    DENSE_RANK() OVER (
        ORDER BY default_rate DESC
    ) AS risk_rank

FROM state_risk

ORDER BY risk_rank;