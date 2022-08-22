### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT *
FROM playlist_track AS A
ORDER BY PlayListId DESC
LIMIT 5;
``` 

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT *
FROM tracks AS B
ORDER BY TrackId 
LIMIT 5;
``` 
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT PlaylistId, Name
FROM playlist_track A INNER JOIN tracks B
  ON A.TrackId = B.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;
```  

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT PlaylistId, Name
FROM playlist_track A INNER JOIN tracks B
  ON A.TrackId = B.TrackId
WHERE playlistId = 10
ORDER BY Name DESC
LIMIT 5;
``` 

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks INNER JOIN artists
  ON tracks.Composer = artists.Name ;
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*)
FROM tracks LEFT OUTER JOIN artists
  ON tracks.Composer = artists.Name;
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
INNER JOIN은 특정 조건에서 일치하는 데이터만 조회하고, 
LEFT JOIN은 왼쪽 테이블의 모든 데이터를 조회하기 때문이다
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceID
LIMIT 5;
``` 

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId
LIMIT 5;
``` 

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceLineId, A.InvoiceId
FROM invoice_items AS A INNER JOIN invoices AS B
  ON A.InvoiceId = B.InvoiceId
ORDER BY A.InvoiceId DESC
LIMIT 5;
``` 


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT A.InvoiceId, A.CustomerId
FROM invoices AS A INNER JOIN Customers AS B
  ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;
``` 

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT itm.InvoiceLineId, ivc.InvoiceId, ivc.CustomerId
FROM invoices AS ivc  
  JOIN invoice_items AS itm
    ON ivc.InvoiceId = itm.InvoiceId
  JOIN customers AS ctm
    ON ivc.CustomerId = ctm.CustomerId
ORDER BY itm.InvoiceId DESC
LIMIT 5;
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT ivc.CustomerId, COUNT(*)
FROM invoices AS ivc
  JOIN invoice_items AS itm
    ON ivc.InvoiceId = itm.InvoiceId
  JOIN customers AS ctm
    ON ivc.CustomerId = ctm.CustomerId
GROUP BY ivc.CustomerId
ORDER BY ivc.CustomerId
LIMIT 5;
```