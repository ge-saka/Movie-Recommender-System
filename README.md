**RECOMMENDER SYSTEM FOR MOVIELENS DATASET**
=======

PHASE 4:GROUP 12 MEMBERS:
=============

Daniel Wahome.

Purity Gitonga.

Brian Kariithi.

Caroline Gesaka.

James Njoroge.


Citation
========

To acknowledge use of the dataset in publications, please cite the following paper:

> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>

INTRODUCTION
=============

In the era of digital content consumption, personalized recommendation systems play a crucial role in enhancing user experience and engagement. Leveraging the MovieLens dataset from the GroupLens research lab, we aim to build an effective movie recommendation system. This system will utilize collaborative filtering techniques to suggest movies based on user ratings, thereby providing personalized movie recommendations.

BUSINESS UNDERSTANDING
========

The primary goal of this project is to enhance user satisfaction by recommending movies that align with their preferences. By analyzing user ratings and movie attributes, we aim to create a system that not only suggests popular or highly rated movies but also discovers niche interests that may not be immediately apparent.

PROBLEM STATEMENT
========

Develop a recommendation system that provides top 5 movie recommendations to users based on their past ratings. The system should address the challenge of sparsity in user ratings and the cold start problem for new users.

OBJECTIVES
========

Build a Collaborative Filtering Model: Implement a collaborative filtering model to recommend movies based on user ratings and similarities between users.

Address the Cold Start Problem: Explore methods to handle new users with limited or no historical data using techniques such as content-based filtering or hybrid approaches.

Evaluate and Optimize: Evaluate the performance of the recommendation system using appropriate metrics and optimize the model to improve recommendation accuracy and coverage.

METRICS OF SUCCESS
========
Recommendation Accuracy: Measure the accuracy of movie recommendations using metrics such as Precision@k and Recall@k.

Coverage: Ensure the system can recommend movies across a wide range of genres and user preferences.

User Engagement: Monitor user engagement metrics, such as click-through rates on recommended movies, to assess the system's effectiveness in improving user interaction.


Content and Use of Files
========================
1. Introduction
   - Objectives and overview.
2. Importing Libraries
   - Essential Python libraries
3. Data Loading and Preprocessing
   - Summary: Loaded and cleaned MovieLens datasets.
   - Findings: Prepared data for analysis.
4. Exploratory Data Analysis (EDA)
   - Summary: Performed statistics and visualizations.
   - Findings: Key patterns in user ratings and popular movies.
5. Collaborative Filtering
   - Summary:Implemented KNN and SVD.
   - Findings: SVD showed superior performance.
6.Content-Based Filterin
   - Summary: Used movie metadata with TF-IDF and cosine similarity.
   - Findings:Recommended similar content effectively.
7.Dimensionality Reduction
   - Summary: Applied SVD.
   - Findings: Enhanced efficiency and performance.
8. Hybrid Recommendations
   - Summary:Combined methods for better accuracy.
   - Findings: Hybrid approach was most effective.
9. Conclusions
   - Summary: Summarized techniques and effectiveness.
   - Findings: Hybrid method performed best.
10. References
    - Sources and datasets.
     
RESULTS
========================

- Collaborative Filtering: Provides personalized recommendations based on similar users' ratings.
- Content-Based Filtering:Suggests movies with similar content.
- Hybrid Recommendations:Combines both methods for more accurate suggestions.
   
CONCLUSION
========================

This project showcases the implementation of a movie recommendation system using the MovieLens dataset. We explored various algorithms and found that the hybrid approach offers the best performance. This project is a practical guide for those interested in recommendation systems.

DEPLOYMENT
========================
https://movielense.streamlit.app/
