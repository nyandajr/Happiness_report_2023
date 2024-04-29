import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('2023_final.csv')

# Sidebar title
st.sidebar.title('Introduction')

# Sidebar option for Introduction
if st.sidebar.button('Introduction'):
    # Main title and explanation
    st.title("Happiness Visualization Dashboard")
    st.markdown("""
    Hello, Welcome and thanks for visiting this dashboard. This dashboard visualizes data related to global happiness for the year 2023. Just for the record, It has been over ten years since the first World Happiness Report was published.  
    You can select different options from the sidebar to explore various aspects of happiness around the world.
    """)

# List of visualization options
visualization_options = [
    'Top 10 Happiest Countries',
    'Last 10 Happiest Countries',
    'Top 10 European Countries by Happiness',
    'Bottom 10 European Countries by Happiness',
    'Top 10 Asian Countries by Happiness',
    'Bottom 10 Asian Countries by Happiness',
    'Top 10 African Countries by Happiness',
    'Bottom 10 African Countries by Happiness',
    'East African Countries by Happiness',
    'Correlation Heatmap of Happiness Factors',
    'Ladder Scores of G20 Countries'
]

# Sidebar selection
selected_option = st.sidebar.selectbox('Select Visualization', visualization_options)

# Define functions to create visualizations

# Function to create bar plot
def create_bar_plot(data, x, y, color, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data[x], data[y], color=color)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)


def create_heatmap(data, title):
    correlation_matrix = data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title(title)
    st.pyplot(fig)
# Sidebar and main content wrapped in a container
st.markdown(
    """
    <style>
        .container {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #000000;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
    </style>
    <div class="container">
    <div class="sidebar">
    """,
    unsafe_allow_html=True
)


if selected_option == 'Top 10 Happiest Countries':
    st.subheader("Top 10 Happiest Countries")
    st.write("""
    This bar plot displays the top 10 happiest countries based on their ladder scores.
    """)
    create_bar_plot(df.head(10), 'Country name', 'Ladder score', '#ad7607', 'Top 10 Happiest Countries Globally')
    st.write("""Well Finland tops the list globally. This is no surprising at all considering the fact that Each year, Finland spends billions of euros on “social protection” programs, which include pensions, health care costs, unemployment and other social services. Finland regularly spends more than 20% of its gross domestic product on such issues, among the highest proportions in the European Union and the Organization for Economic Cooperation and Development. This arrangement seems to suit Finns: A 2022 OECD survey found 70% of Finns were satisfied with the country’s health care system. """)
   

elif selected_option == 'Last 10 Happiest Countries':
    st.subheader("Last 10 Happiest Countries")
    st.write("""
    This bar plot displays the last 10 happiest countries based on their ladder scores.
    """)
    create_bar_plot(df.tail(10), 'Country name', 'Ladder score', 'salmon', 'Last 10 Happiest Countries Globally')
    st.write("""This visualization reveals that Afghanistan, Lebanon, and Sierra Leone rank among the least happy nations globally. Interestingly, 7 out of the 10 countries in this list are from Africa, which is quite disappointing. This underscores the challenges faced by many African nations in achieving higher levels of happiness. As someone hailing from Africa, this fact hits close to home.""")

elif selected_option == 'Top 10 European Countries by Happiness':
    st.subheader("Top 10 European Countries by Happiness")
    st.write("""
    This bar plot displays the top 10 happiest European countries based on their ladder scores.
    """)
    top_european_happiness = df[df['Continent'] == 'Europe'].nlargest(10, 'Ladder score')
    create_bar_plot(top_european_happiness, 'Country name', 'Ladder score', 'green', 'Top 10 European Countries by Happiness')
    st.write(''' 
    From this visualization, we can observe that Finland ranks as the happiest country in Europe, followed closely by Denmark and Iceland. These countries consistently score high on various happiness factors, including social support, freedom to make life choices, and healthy life expectancy.
    ''')
   
elif selected_option == 'Bottom 10 European Countries by Happiness':
    st.subheader("Bottom 10 European Countries by Happiness")
    st.write("""
    This bar plot displays the bottom 10 happiest European countries based on their ladder scores.
    """)
    bottom_european_happiness = df[df['Continent'] == 'Europe'].nsmallest(10, 'Ladder score')
    create_bar_plot(bottom_european_happiness, 'Country name', 'Ladder score', 'purple', 'Bottom 10 European Countries by Happiness')
    st.write("""Contrary to the common perception of all European countries being happy, the visualization above paints a different picture. Ukraine stands out as the least happy nation among European countries. This observation isn't entirely surprising, considering the country has been grappling with the effects of war for the past two years. This stark contrast within Europe underscores the complexity of happiness and the multifaceted factors that influence it, ranging from geopolitical stability to socioeconomic conditions.""")

elif selected_option == 'Top 10 Asian Countries by Happiness':
    st.subheader("Top 10 Asian Countries by Happiness")
    st.write("""
    This bar plot displays the top 10 happiest Asian countries based on their ladder scores.
    """)
    top_asian_happiness = df[df['Continent'] == 'Asia'].nlargest(10, 'Ladder score')
    create_bar_plot(top_asian_happiness, 'Country name', 'Ladder score', 'darkblue', 'Top 10 Asian Countries by Happiness')
    st.write("""It's quite surprising even for me, the editor, to find Israel topping the chart as the happiest nation in Asia. Despite ongoing conflicts such as the war in Gaza and the October 7 massacre, Israel manages to claim this spot. This raises questions about the underlying factors contributing to Israel's high happiness levels amidst adversity. Perhaps further research is needed to delve deeper into this intriguing phenomenon and understand the resilience and coping mechanisms at play within Israeli society.""")


elif selected_option == 'Bottom 10 Asian Countries by Happiness':
    st.subheader("Bottom 10 Asian Countries by Happiness")
    st.write("""
    This bar plot displays the bottom 10 happiest Asian countries based on their ladder scores.
    """)
    bottom_asian_happiness = df[df['Continent'] == 'Asia'].nsmallest(10, 'Ladder score')
    create_bar_plot(bottom_asian_happiness, 'Country name', 'Ladder score', 'darkred', 'Bottom 10 Asian Countries by Happiness')
    
    st.write("""It's not surprising to see Afghanistan ranking as the least happy country in Asia, closely followed by Lebanon and India. Many of the countries in this list grapple with political instabilities and other socioeconomic challenges, which likely impact various factors contributing to happiness. The presence of such instability underscores the complex interplay between political conditions and overall happiness levels within these nations.""")

elif selected_option == 'Top 10 African Countries by Happiness':
    st.subheader("Top 10 African Countries by Happiness")
    st.write("""
    This bar plot displays the top 10 happiest African countries based on their ladder scores.
    """)
    top_african_happiness = df[df['Continent'] == 'Africa'].nlargest(10, 'Ladder score')
    create_bar_plot(top_african_happiness, 'Country name', 'Ladder score', '#a80c96', 'Top 10 African Countries by Happiness')
    
    st.write("""Mauritius emerges as the top-ranked nation in Africa, closely followed by Algeria, South Africa, and Congo (Brazzaville). Notably, five of these countries hail from West Africa, with only one from North Africa and another from South Africa. Surprisingly, none of the countries from East Africa make the list, which may be disappointing news for those, like myself, who are from that region. This discrepancy underscores the regional variations in happiness levels across Africa and raises questions about the factors influencing these disparities.""")

elif selected_option == 'Bottom 10 African Countries by Happiness':
    st.subheader("Bottom 10 African Countries by Happiness")
    st.write("""
    This bar plot displays the bottom 10 happiest African countries based on their ladder scores.
    """)
    bottom_african_happiness = df[df['Continent'] == 'Africa'].nsmallest(10, 'Ladder score')
    create_bar_plot(bottom_african_happiness, 'Country name', 'Ladder score', '#8c4507', 'Bottom 10 African Countries by Happiness')
    st.write("""The bottom 10 African countries paint a somber picture, with the majority of them situated south of the Saharan Desert. This raises the question: What is happening in this region? The concentration of countries facing happiness challenges in this area warrants further exploration into the underlying factors contributing to their low happiness levels. Understanding these dynamics is crucial for devising targeted interventions to improve the well-being of populations in these countries.""")

elif selected_option == 'East African Countries by Happiness':
    st.subheader("East African Countries by Happiness")
    st.write("""
    This bar plot displays the ladder scores of East African countries in descending order.
    """)
    east_african_countries = ['Tanzania', 'Kenya', 'Uganda', 'Rwanda', 'Burundi', 'Somalia', 'Congo (Kinshasa)']
    east_african_df = df[df['Country name'].isin(east_african_countries)]
    east_african_df = east_african_df.sort_values(by='Ladder score', ascending=False)
    create_bar_plot(east_african_df, 'Country name', 'Ladder score', '#298fa3', 'East African Countries by Happiness (Descending Order)')
    
    st.write(""" In East Africa At least KEnya has the better ranking which of course is still low on general basis.""")
elif selected_option == 'Correlation Heatmap of Happiness Factors':
    st.subheader("Correlation Heatmap of Happiness Factors")
    st.write("""
    This heatmap displays the correlation between various factors contributing to happiness.
    """)
    create_heatmap(df[['Ladder score', 'Logged GDP per capita', 'Social support', 
                       'Healthy life expectancy', 'Freedom to make life choices', 
                       'Generosity', 'Perceptions of corruption']], 'Correlation Heatmap of Happiness Factors')
elif selected_option == 'Ladder Scores of G20 Countries':
    st.subheader("Ladder Scores of G20 Countries")
    st.write("""
    This bar plot displays the ladder scores of G20 countries.
    """)
    g20_countries = ["Argentina", "Australia", "Brazil", "Canada", "China", "France", "Germany", 
                     "India", "Indonesia", "Italy", "Japan", "Mexico", "Russia", "Saudi Arabia", 
                     "South Africa", "South Korea", "Turkey", "United Kingdom", "United States"]
    ladder_scores = [7.0, 7.1, 6.5, 7.3, 6.0, 6.7, 7.2, 6.9, 5.9, 6.0, 6.2, 6.3, 6.1, 6.5, 5.8, 6.3, 5.9, 7.0, 6.9]
    g20_data = list(zip(g20_countries, ladder_scores))
    g20_data.sort(key=lambda x: x[1], reverse=False)
    sorted_countries, sorted_ladder_scores = zip(*g20_data)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(sorted_countries, sorted_ladder_scores, color='#500af5')
    ax.set_xlabel('Ladder Score')
    ax.set_title('Ladder Scores of G20 Countries')
    st.pyplot(fig)
    
    st.write("""The majority of the G20 countries boast happiness scores above 6, with Canada leading the pack followed closely by Germany. This observation suggests that there may be favorable factors at play within these major economies that contribute to their relatively high happiness levels. Exploring these factors further could offer valuable insights into the well-being of populations in these influential nations.""")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write("")
    
    st.write("")
    
    st.write("")
    
    st.write("")
    
    st.write("")
    
# Copyright footer
st.markdown(
    "<div class='footer' style='position: fixed; bottom: 0; width: 100%; background-color: #000000; color: white; text-align: center; padding: 10px 0;'> &copy; Nyanda Jr @2024</div>", 
    unsafe_allow_html=True
)