'''
Created on 2015.11.28

@author: ju
'''
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse import linalg
import scipy.sparse

voltagesourcebranch=\
np.array([
          [1,-1,0]
          ])
constbranch=\
np.array([
          [1,4,4],
          [1,3,2.5]
          ])
closedcb=\
np.array([
          [4,2,0],
          [3,4,0],                  
          ])
opencb=\
np.array([
          [5,2,0.0],  
          ])
#frnode,tonode,branchidx
voltagecontrolbranch=np.array([
[3,5,5]                              
                               ])
currentsourcebranch=\
np.array([
          [2,-1,0.4],
          [3,-1,0.8]
          ])

nnodes=5
nbranches=9
nodedict={}
for i in range(5):
    nodedict[i+1]=i
#print nodedict
Arow=[]
Acol=[]
Adata=[]
frow=[]
fcol=[]
fdata=[]
rval=[]
for i in range(nnodes+2*nbranches):
    rval.append(0.0)
idxbranch=0

for i in range(len(voltagesourcebranch)):
    item=voltagesourcebranch[i]
    frnode=int(item[0])
    tonode=int(item[1])
    if not frnode==-1:
        Arow.append(nodedict[frnode])
        Acol.append(idxbranch)
        Adata.append(1.0)
    if not tonode==-1:
        Arow.append(nodedict[tonode])
        Acol.append(idxbranch)
        Adata.append(-1.0)
    frow.append(idxbranch)
    fcol.append(idxbranch+nnodes)
    fdata.append(1.0)           
    rval[nnodes+nbranches+idxbranch]=float(item[2])
    idxbranch=idxbranch+1

for i in range(len(constbranch)):
    item=constbranch[i]
    frnode=int(item[0])
    tonode=int(item[1])
    if not frnode==-1:
        Arow.append(nodedict[frnode])
        Acol.append(idxbranch)
        Adata.append(1.0)
    if not tonode==-1:
        Arow.append(nodedict[tonode])
        Acol.append(idxbranch)
        Adata.append(-1.0)
    frow.append(idxbranch)
    fcol.append(idxbranch+nnodes)
    fdata.append(item[2])
    frow.append(idxbranch)
    fcol.append(idxbranch+nbranches+nnodes)
    fdata.append(-1.0)               
    rval[nnodes+nbranches+idxbranch]=0.0
    idxbranch=idxbranch+1

for i in range(len(closedcb)):
    item=closedcb[i]
    frnode=int(item[0])
    tonode=int(item[1])
    if not frnode==-1:
        Arow.append(nodedict[frnode])
        Acol.append(idxbranch)
        Adata.append(1.0)
    if not tonode==-1:
        Arow.append(nodedict[tonode])
        Acol.append(idxbranch)
        Adata.append(-1.0)
    frow.append(idxbranch)
    fcol.append(idxbranch+nnodes)
    fdata.append(1.0)           
    rval[nnodes+nbranches+idxbranch]=float(item[2])
    idxbranch=idxbranch+1
   
for i in range(len(opencb)):
    item=opencb[i]
    frnode=int(item[0])
    tonode=int(item[1])
    if not frnode==-1:
        Arow.append(nodedict[frnode])
        Acol.append(idxbranch)
        Adata.append(1.0)
    if not tonode==-1:
        Arow.append(nodedict[tonode])
        Acol.append(idxbranch)
        Adata.append(-1.0)
    frow.append(idxbranch)
    fcol.append(idxbranch+nbranches+nnodes)
    fdata.append(1.0)           
    rval[nnodes+nbranches+idxbranch]=float(item[2])
    idxbranch=idxbranch+1

for i in range(len(voltagecontrolbranch)):
    item=voltagecontrolbranch[i]
    frnode=int(item[0])
    tonode=int(item[1])
    if not frnode==-1:
        Arow.append(nodedict[frnode])
        Acol.append(idxbranch)
        Adata.append(1.0)
    if not tonode==-1:
        Arow.append(nodedict[tonode])
        Acol.append(idxbranch)
        Adata.append(-1.0)
    frow.append(idxbranch)
    fcol.append(idxbranch+nnodes)
    fdata.append(1.0)
    frow.append(idxbranch)
    fcol.append(int(item[2])+nnodes)
    fdata.append(-1.0)               
    rval[nnodes+nbranches+idxbranch]=0.0
    idxbranch=idxbranch+1
    
for i in range(len(currentsourcebranch)):
    item=currentsourcebranch[i]
    frnode=int(item[0])
    tonode=int(item[1])
    if not frnode==-1:
        Arow.append(nodedict[frnode])
        Acol.append(idxbranch)
        Adata.append(1.0)
    if not tonode==-1:
        Arow.append(nodedict[tonode])
        Acol.append(idxbranch)
        Adata.append(-1.0)
    frow.append(idxbranch)
    fcol.append(idxbranch+nbranches+nnodes)
    fdata.append(1.0)           
    rval[nnodes+nbranches+idxbranch]=float(item[2])
    idxbranch=idxbranch+1

#print Arow
#print Acol
#print Adata
row = np.array(Arow)
col = np.array(Acol)
data = np.array(Adata)
A=csr_matrix((data, (row, col)), shape=(nnodes,nbranches))


row = np.array(Acol)
col = np.array(Arow)
data = np.array(Adata)
AT=csr_matrix((data, (row, col)), shape=(nbranches,nnodes))


zeromat1=csr_matrix((nnodes,nnodes+nbranches))
zeromat2=csr_matrix((nbranches,nbranches))
J1=scipy.sparse.hstack([zeromat1,A],format='csr')
row=[]
col=[]
data=[]
for i in range(nbranches):
    row.append(i)
    col.append(i)
    data.append(-1.0)
row=np.array(row)
col=np.array(col)
data=np.array(data)    
minusidentity=csr_matrix((data, (row, col)), shape=(nbranches,nbranches))
J2=scipy.sparse.hstack([AT,minusidentity,zeromat2],format='csr')
row=np.array(frow)
col=np.array(fcol)
data=np.array(fdata)
f=csr_matrix((data, (row, col)), shape=(nbranches,2*nbranches+nnodes))
print f.todense()
J=scipy.sparse.vstack([J1,J2,f],format='csr')
F=rval
x=linalg.spsolve(J, F)
for i in range(nbranches):
    print 'branch current',i,x[nnodes+nbranches+i]


    
    

