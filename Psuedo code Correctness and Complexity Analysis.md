## Correctness 

## Complexity Analysis
```
function lcslen(X[1..m], Y[1..n]) 
C = [[for i =0 to (len(Y) + 1)] for j= 0 to (len(X+ 1)]--nm 
for i, X[i] to enumerate(X)-----------------n+1  
for j, Y[i] to enumerate(Y) ----------------n(m+1) 
 if X[I] == Y[j] ---------------------------nm 
  C[i][j] = 1 + C[i-1][j-1]------------------  
else  
C[i][j] = max(C[i][j-1], C[i-1][j]) ----------- 
return C------------------------------1 

T(n)=(n+1)+n(m+1)+nm+1+nm 
T(n)=n+1+nm+n+nm+1+nm 
T(n)=2n+3nm+2  

function backtrack(C[0..m,0..n], X[1..m], Y[1..n], i, j)  
if i = 0 or j = 0 --------------------1 
return ""  
if X[i] == Y[j] ----------------------1 
 return backtrack(C, X, Y, i-1, j-1) + X[i]  
if C[i,j-1] > C[i-1,j]----------------1  
 return backtrack(C, X, Y, i, j-1)  
return backtrack(C, X, Y, i-1, j)---------1 
T(n)=T(n)+4 
 
function lcs(X[1..m], Y[1..n])  
C=lcs(X, Y) -----------------------1 
return backtrack(C, X, Y,len(X-1),len(X,-1)) ------------1 
T(n)=2 

function Checker(C[0...m,0...n],x[1...m],Y[1...n],i,j) 
if i<0 and j<0--------------n 
return-------------------1  
elseif i<0-----------------n 
 Checker(C,X,Y,i,j-1)-------1 
 print "+" + Y[j] 
elseif j<0-----------------n 
 Checker(C,X,Y,i-1,j) -------1 
 print "-" + X[i] 
elseif X[i] == Y[j]----------n 
 Checker(C,X,Y,i-1,j-1) -------1 
 print " " + X[i] 
elseif C[i][j-1] >= C[i-1][j]---------n 
 Checker(C,X,Y,i,j-1) -------1 
 print "+" + Y[j] 
elseif C[i][j-1] < C[i-1][j]----------n 
 Checker(C,X,Y,i-1,j) -------1 
 print "-" + X[i] 

T(n)=6n+6 
 
function Check(X,Y) 
C = lcslen(X,Y)-------------1 
return Checker(C,X,Y,len(X)-1,len(Y)-1)---------------1 

T(n)=2 