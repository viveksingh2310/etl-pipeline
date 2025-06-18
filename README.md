# etl-pipeline
This project demonstrates a complete end-to-end ETL (Extract, Transform, Load) pipeline using PySpark, integrated with a Streamlit-based interactive frontend to visualize stock market data. Over the course of 24 months of simulated Infosys stock prices, the pipeline performs essential data cleaning and transformation tasks—such as calculating moving averages—and stores the processed data for visualization.

The dashboard allows users to:
<ul>
Trigger the ETL process in real time.

Visualize trends in closing prices, trading volume, and moving averages.

Explore raw and transformed data interactively.
</ul>
This project showcases how big data tools like Apache Spark can be seamlessly combined with lightweight web frameworks like Streamlit to deliver insightful, interactive data analytics in real-world financial applications. It serves as a solid foundation for building scalable dashboards, integrating live APIs, or expanding into advanced technical indicators.



![Screenshot 2025-06-18 193545](https://github.com/user-attachments/assets/090bc2a9-4d4f-43a2-9e6e-ccba9d796942)

After successfully running the ETL file we have the following output present at the <b>output subfolder of the project in CSV format:</b>

![Screenshot 2025-06-18 194219](https://github.com/user-attachments/assets/bf0b0050-50c8-4890-a2aa-de291f838ffd)


This is the input data which is present as initial dataset of the project:

![Screenshot 2025-06-18 193959](https://github.com/user-attachments/assets/2205ab2e-9443-4bb3-a8b0-93c33b618b9b)

Here is the screenshot of the terminal through which streamlit is being run:

![Screenshot 2025-06-18 193849](https://github.com/user-attachments/assets/7b6b321e-53fc-4d58-827e-94b5d0daaa50)


