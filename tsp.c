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
            (*dis)[i][j]=sqrt(pow(pos[i][0]-pos[j][0],2)+pow(pos[i][1]-pos[j][1],2));
    }
}

void buildset(long n,long *set)
{
    long i,ne,p,count;
    long *temp,j;
    ne = pow(2,n-1);
    temp = (long*)malloc(sizeof(long)*ne);

    for(i=0;i<ne;i++)
    {   
        count=0;
        for(p=1;p<=i;p=p<<1)
            if (i&p)
                ++count;
        set[i]=count;
        temp[i]=i;
    }
    // sort set by count and return index: very slow!!
    i=ne;
    while(i>0)
    {
        for(j=0;j<i-1;j++)
        {
            if(set[j]>set[j+1])
            {
                p = set[j];
                set[j]=set[j+1];
                set[j+1]=p;
                p = temp[j];
                temp[j] = temp[j+1];
                temp[j+1]=p;
            }
        }
    }
    for(i=0;i<ne;i++)
        set[i]=temp[i];
    free(temp);
}

void search(float **dis, long *set, long n)
{
    long nset,nelement,i,j,m,index,nm;
    double **a;
    nset = (long)(pow(2,n-1));
    a = (double**)malloc(n*sizeof(double));
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
        nm = m<n-m?m:n-m;
        for (i=0;i<nm;i++)
            nelement*=n-i-1;
        for (i=0;i<nm;i++)
            nelement/=i+1;
        printf("Processing .. %ld / %ld, for %ld cases\n",m,n,nelement);
        for (i=0;i<nelement;i++)
        {
            for(j=1;j<n;j++)
            {
                // check j in subset set[index]
                if (set[index] & (long)(pow(2,j)))
                {
                    printf("%ld %ld %ld %ld\n",i,j,set[index],(long)(pow(2,j)));
                    // NEED TO FINISH!!
                }
            }
            index++;
        }
    }
    
    // clean up
    for(i=0;i<n;i++)
        free(a[i]);
    free(a);
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
