# Plagiarism-Checkrista
## Plagiarism checking tool 
### Psuedo Code
```
function Checker(C[0...m,0...n],x[1...m],Y[1...n],i,j)
 if i<0 and j<0
  return 
 elseif i<0
  Checker(C,X,Y,i,j-1)
  print "+" + Y[j]
 elseif j<0
  Checker(C,X,Y,i-1,j)
  print "-" + X[i]
 elseif X[i] == Y[j]
  Checker(C,X,Y,i-1,j-1)
  print " " + X[i]
 elseif C[i][j-1] >= C[i-1][j]
  Checker(C,X,Y,i,j-1)
  print "+" + Y[j]
 elseif C[i][j-1] < C[i-1][j]
  Checker(C,X,Y,i-1,j)
  print "-" + X[i]

function Check(X,Y)
 C = lcslen(X,Y)
 return Checker(C,X,Y,len(X)-1,len(Y)-1)

function backtrack(C[0..m,0..n], X[1..m], Y[1..n], i, j) 
 if i = 0 or j = 0 
  return "" 
 if X[i] == Y[j] 
  return backtrack(C, X, Y, i-1, j-1) + X[i] 
 if C[i,j-1] > C[i-1,j] 
  return backtrack(C, X, Y, i, j-1) 
 return backtrack(C, X, Y, i-1, j) 

function lcs(X[1..m], Y[1..n]) 
 C=lcs(X, Y) 
 return backtrack(C, X, Y,len(X-1),len(X,-1)) 
 
function lcslen(X[1..m], Y[1..n]) 
 C = [[for i =0 to (len(Y) + 1)] 
        for j= 0 to (len(X+ 1)] 
           for i, X[i] to enumerate(X) 
              for j, Y[i] to enumerate(Y) 
                  if X[I] == Y[j] 
                    C[i][j] = 1 + C[i-1][j-1] 
                  else 
                    C[i][j] = max(C[i][j-1], C[i-1][j]) 
 return C 
 ```
