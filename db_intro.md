# 仿生水膠資料庫介紹
## 環境介紹
資料庫：MariaDB 10.5.6<br>
容器名稱：geldb_mariadb<br>
端口：3306 → 3306/tcp

## 資料庫內容
### 資料庫種類
| 資料庫 | 表格 |
|:---| :---|
| experiment | 
| simulation |
| analysis |

### 使用者權限
使用者可分成三種身份進入資料庫：
| 身份           | 權限       | 帳號            | 密碼       |
| :--- | :--- | :--- | :--- |
| **Experiment** | experiment | experiment_user | experiment |
| **Simulation** | simulation | simulation_user | simulation |
| **Analysis** | analysis | analysis_user | analysis |

 

