#include<stdio.h>
#define GSIZE (20)
#define WHITE 0
#define GRAY 1
#define BLACK 2

#define TRUE 1
#define FALSE 0


struct queue{
	int arr[100];
	int front;
	int rear;
};
void init_queue(struct queue* q){
	q->rear = -1;
	q->front = 0;
}
int empty_queue(struct queue* q){
	if(q->rear < q->front) return TRUE;
	return FALSE;
}
void insert_queue(struct queue* q, int e){
	q->rear = q->rear + 1;
	q->arr[q->rear] = e;
}
int delete_queue(struct queue* q){
	int e = q->arr[q->front];
	q->front = q->front + 1;
	return e;
}
struct graph{
	int A[GSIZE][GSIZE];
	int n;
	int bfscol[GSIZE];
	int bfsdist[GSIZE];
	int bfspred[GSIZE];
};

void create_graph(struct graph* g){
	g->n = 8;
	for(int i=0; i<20; ++i){
		for(int j=0; j<20; ++j){
			g->A[i][j] = 0;		
		}		
	}
	g->A[0][1] = 1;
	g->A[1][0] = 1;
	
	g->A[2][1] = 1;
	g->A[1][2] = 1;
	
	g->A[2][5] = 1;
	g->A[5][2] = 1;
	
	g->A[2][3] = 1;
	g->A[3][2] = 1;
	
	g->A[4][3] = 1;
	g->A[3][4] = 1;
	
	g->A[5][3] = 1;
	g->A[3][5] = 1;
	
	g->A[5][4] = 1;
	g->A[4][5] = 1;	
}

void BFS(struct graph* g, int s){

	for(int i=0; i<g->n; ++i){
		g->bfscol[i] = WHITE;
		g->bfsdist[i] = -1;
		g->bfspred[i] = -2;
	}
	g->bfsdist[s] = 0;
	g->bfspred[s] = -1;
	g->bfscol[s] = GRAY;
	struct queue q;
	init_queue(&q);
	insert_queue(&q, s);

	while(empty_queue(&q) != TRUE){
		int u = delete_queue(&q);

		for(int v=0; v<g->n; ++v){
			int a = g->A[u][v];

			a = g->bfscol[v];

			if(g->A[u][v] == 1 && g->bfscol[v] == WHITE){

				g->bfscol[v] = GRAY;
				g->bfsdist[v] = g->bfsdist[u] + 1;
				g->bfspred[v] = u;
				insert_queue(&q, v);
			}

		}
		g->bfscol[u] =BLACK;

	}	
}

int main(){
	printf("Hello, World!\n");
	struct graph g;

	create_graph(&g);

	BFS(&g, 2);

	for(int i=0; i<g.n; ++i){
		printf("col=%4d, dist=%4d, pred=%4d\n", g.bfscol[i], g.bfsdist[i], g.bfspred[i]);
	}
}
