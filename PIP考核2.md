# 使用open3D完成云点聚类任务生成云点图

## 如何思考

*   了解云点聚类是要实现什么
*   了解进行聚类任务所需的算法
*   了解代码细节
*   如何实现可视化

## 参考资料

*   [https://blog.csdn.net/weixin\_50514171/article/details/127195711?ops\_request\_misc=%257B%2522request%255Fid%2522%253A%25224CAA218F-61B7-4230-8CA8-C20816259ECA%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D\&request\_id=4CAA218F-61B7-4230-8CA8-C20816259ECA\&biz\_id=0\&utm\_medium=distribute.pc\_search\_result.none-task-blog-2~all~top\_positive\~default-2-127195711-null-null.142^v100^control\&utm\_term=dbscan%E7%AE%97%E6%B3%95\&spm=1018.2226.3001.4187]()

    *   [https://blog.csdn.net/pursue\_dreams/article/details/134479790?ops\_request\_misc=%257B%2522request%255Fid%2522%253A%2522575DEF15-F0C4-43B1-B53A-7A2E0B2D7A27%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D\&request\_id=575DEF15-F0C4-43B1-B53A-7A2E0B2D7A27\&biz\_id=0\&utm\_medium=distribute.pc\_search\_result.none-task-blog-2~all~first\_rank\_ecpm\_v1\~rank\_v31\_ecpm-1-134479790-null-null.142^v100^control\&utm\_term=Open3D%E8%BF%9B%E8%A1%8C%E7%82%B9%E4%BA%91%E8%81%9A%E7%B1%BB%E4%BB%BB%E5%8A%A1%E5%B9%B6%E7%94%9F%E6%88%90%E8%81%9A%E7%B1%BB%E5%90%8E%E7%9A%84%E7%82%B9%E4%BA%91%E5%9B%BE\&spm=1018.2226.3001.4187](https://blog.csdn.net/pursue_dreams/article/details/134479790?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522575DEF15-F0C4-43B1-B53A-7A2E0B2D7A27%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D\&request_id=575DEF15-F0C4-43B1-B53A-7A2E0B2D7A27\&biz_id=0\&utm_medium=distribute.pc_search_result.none-task-blog-2\~all\~first_rank_ecpm_v1\~rank_v31_ecpm-1-134479790-null-null.142^v100^control\&utm_term=Open3D%E8%BF%9B%E8%A1%8C%E7%82%B9%E4%BA%91%E8%81%9A%E7%B1%BB%E4%BB%BB%E5%8A%A1%E5%B9%B6%E7%94%9F%E6%88%90%E8%81%9A%E7%B1%BB%E5%90%8E%E7%9A%84%E7%82%B9%E4%BA%91%E5%9B%BE\&spm=1018.2226.3001.4187)

*   &#x20;[https://blog.csdn.net/jane0819/article/details/131792041?ops\_request\_misc=%257B%2522request%255Fid%2522%253A%2522A1F0E0CC-E07F-455B-8F5E-6B9065089F1B%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D\&request\_id=A1F0E0CC-E07F-455B-8F5E-6B9065089F1B\&biz\_id=0\&utm\_medium=distribute.pc\_search\_result.none-task-blog-2~all~sobaiduend\~default-1-131792041-null-null.142^v100^control\&utm\_term=%E9%A2%84%E5%A4%84%E7%90%86%E7%82%B9%E4%BA%91\&spm=1018.2226.3001.4187](https://blog.csdn.net/jane0819/article/details/131792041?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522A1F0E0CC-E07F-455B-8F5E-6B9065089F1B%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D\&request_id=A1F0E0CC-E07F-455B-8F5E-6B9065089F1B\&biz_id=0\&utm_medium=distribute.pc_search_result.none-task-blog-2\~all\~sobaiduend\~default-1-131792041-null-null.142^v100^control\&utm_term=%E9%A2%84%E5%A4%84%E7%90%86%E7%82%B9%E4%BA%91\&spm=1018.2226.3001.4187)

*   [https://blog.csdn.net/qq\_46322529/article/details/128204905?ops\_request\_misc=%257B%2522request%255Fid%2522%253A%2522FA03D175-A61A-43B2-8DE8-ABFE733EC766%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D\&request\_id=FA03D175-A61A-43B2-8DE8-ABFE733EC766\&biz\_id=0\&utm\_medium=distribute.pc\_search\_result.none-task-blog-2~all~first\_rank\_ecpm\_v1\~rank\_v31\_ecpm-6-128204905-null-null.142^v100^control\&utm\_term=Open3D%E8%BF%9B%E8%A1%8C%E7%82%B9%E4%BA%91%E8%81%9A%E7%B1%BB%E4%BB%BB%E5%8A%A1%E5%B9%B6%E7%94%9F%E6%88%90%E8%81%9A%E7%B1%BB%E5%90%8E%E7%9A%84%E7%82%B9%E4%BA%91%E5%9B%BE\&spm=1018.2226.3001.4187](https://blog.csdn.net/qq_46322529/article/details/128204905?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522FA03D175-A61A-43B2-8DE8-ABFE733EC766%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D\&request_id=FA03D175-A61A-43B2-8DE8-ABFE733EC766\&biz_id=0\&utm_medium=distribute.pc_search_result.none-task-blog-2\~all\~first_rank_ecpm_v1\~rank_v31_ecpm-6-128204905-null-null.142^v100^control\&utm_term=Open3D%E8%BF%9B%E8%A1%8C%E7%82%B9%E4%BA%91%E8%81%9A%E7%B1%BB%E4%BB%BB%E5%8A%A1%E5%B9%B6%E7%94%9F%E6%88%90%E8%81%9A%E7%B1%BB%E5%90%8E%E7%9A%84%E7%82%B9%E4%BA%91%E5%9B%BE\&spm=1018.2226.3001.4187)

## 实现功能

1.  预处理点云
2.  进行聚类
3.  将结果可视化
4.  保存聚类后文件

## 学习内容

学习到了GitHub使用方式，搜索他人开源代码，建立公共库进行代码共享等操作
