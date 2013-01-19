/* TSP problem solver 
   Based on q5.py
 */

#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define LARGENUM 1e20

long loadtable(char *fname, float ***pos)
{
    FILE *fp;
    char line[500];    
    int n,i;
    fp = fopen(fname,"r");
    fgets(line,500,fp);
    sscanf(line,"%d",&n);
    *pos = (float **)malloc(n*sizeof(float*));
    for (i=0;i<n;i++)
    {
        fgets(line,500,fp);
        (*pos)[i] = (float*)malloc(2*sizeof(float));
        sscanf(line,"%f %f",&((*pos)[i][0]),&((*pos)[i][1]));
    }
    fclose(fp);
    return n;
}

void computedist(int n, float**pos, float***dis)
{
    int i,j;
    *dis = (float **)malloc(n*sizeof(float*));
    for (i=0;i<n;i++)
    {
        (*dis)[i] = (float *)malloc(n*sizeof(float));
        for(j=0;j<n;j++)
        {
            (*dis)[i][j]=sqrt(pow(pos[i][0]-pos[j][0],2)+pow(pos[i][1]-pos[j][1],2));
        }
    }
}

void buildset(long n,long *set)
{
    long i,ne,p,count,j,index;
    ne = pow(2,n-1);


    index=0;
    for(j=0;j<=n;j++)
    {
        for(i=0;i<ne;i++)
        {
            count=0;
            for(p=1;p<=i;p=p<<1)
                if (i&p)
                    ++count;
            if(count==j)
            {
                set[index]=i;
                index++;
            }
        }
    }
//    for (i=0;i<ne;i++) printf("%ld ",set[i]);
//    printf("\n");
}

void search(float **dis, long *set, long n)
{
    long nset,nelement,i,j,k,m,index,nm,target;
    double **a;
    double *len,min;
    int it;
    
    nset = (long)(pow(2,n-1));
    a = (double**)malloc(n*sizeof(double));
    len = (double*)malloc(n*sizeof(double));
    for(i=0;i<n;i++)
    {
        a[i] = (double*)malloc(nset*sizeof(double));
        for(j=0;j<nset;j++)
            a[i][j]=LARGENUM;
    }
    a[0][0]=0;
    index=1;
    // start search
    for (m=1;m<n;m++) // loop all subproblem size
    {
        nelement=1;
        nm = m<n-m-1?m:n-m-1;
        for (i=0;i<nm;i++)
            nelement*=n-i-1;
        for (i=0;i<nm;i++)
            nelement/=i+1;
        printf("Processing .. %ld / %ld for %ld cases\n",m,n,nelement);
        for (i=0;i<nelement;i++)
        {
            for(j=1;j<n;j++)
            {
                // check j in subset set[index]
                if (set[index] & (long)(pow(2,j-1)))
                {
                    //printf("%ld %ld %ld\n",index,set[index],(long)(pow(2,j)));
                    // NEED TO FINISH!!
                    for (it=0;it<n;it++) len[it]=LARGENUM;
                    target = set[index]-(long)(pow(2,j-1));
                    len[0]=a[0][target]+dis[0][j];
                    for(k=1;k<n;k++)
                        if (set[index] & (long)(pow(2,k-1))) // check k in set[index]
                        {
                            len[k]=a[k][target]+dis[k][j];
                        }
                    min=LARGENUM;
                    for (k=0;k<n;k++)
                        if (len[k]<min) min=len[k];
                    a[j][set[index]]=min;
                }
            }
            index++;
        }
    }
    for (it=0;it<n;it++) len[it]=LARGENUM;
    for(i=1;i<n;i++)
    {
        len[i]=a[i][nset-1]+dis[0][i];
    }
    min = LARGENUM;
    for (k=0;k<n;k++)
        if (len[k]<min) min=len[k];
    printf("%lf\n",min);
    // clean up
    for(i=0;i<n;i++)
        free(a[i]);
    free(a);
    free(len);
}

int main(int argc, char*argv[])
{
    float **pos,**dis;
    int n,i;
    long *set;

    printf("# start to build map\n");
    n = loadtable(argv[1],&pos);
    computedist(n,pos,&dis);
    set = (long*)malloc(pow(2,n-1)*sizeof(long));

    buildset(n,set);

    printf("# start to search map\n");
    search(dis,set,n);

    for(i=0;i<n;i++)
    {
        free(pos[i]);
        free(dis[i]);
    }
    free(pos);
    free(dis);
    free(set);
    return 0;
}
