import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go

def show_evaluation():
    # Page title
    st.markdown("<h1 style='text-align: center;'>Evaluasi Data Prediksi Liver</h1>", unsafe_allow_html=True)
    
    if os.path.exists('new_patient_data.csv'):
        # Load the collected data
        collected_data = pd.read_csv('new_patient_data.csv')
        
        # Calculate statistics
        total_data = len(collected_data)
        positive_cases = len(collected_data[collected_data['prediction'] == 1])
        negative_cases = len(collected_data[collected_data['prediction'] == 0])
        
        # Create three columns for statistics
        col1, col2, col3 = st.columns(3)
        
        # Style for the metrics
        metric_style = """
        <style>
            .metric-card {
                background-color: #f0f2f6;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .metric-value {
                font-size: 36px;
                font-weight: bold;
                color: #0066cc;
                margin: 10px 0;
            }
            .metric-label {
                font-size: 16px;
                color: #666;
            }
        </style>
        """
        st.markdown(metric_style, unsafe_allow_html=True)
        
        # Display metrics in cards
        with col1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{total_data}</div>
                    <div class="metric-label">Total Data Terkumpul</div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        with col2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{positive_cases}</div>
                    <div class="metric-label">Kasus Positif</div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
        with col3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-value">{negative_cases}</div>
                    <div class="metric-label">Kasus Negatif</div>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        # Add some spacing
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Display donut chart for case distribution
        fig = go.Figure(data=[go.Pie(
            labels=['Kasus Positif', 'Kasus Negatif'],
            values=[positive_cases, negative_cases],
            hole=.3,
            marker_colors=['#FF6B6B', '#4ECDC4']
        )])
        
        fig.update_layout(
            title_text="Distribusi Kasus",
            showlegend=True,
            width=400,
            height=400
        )
        
        st.plotly_chart(fig)
        
        # Display the collected data table
        st.markdown("### Data yang Telah Terkumpul")
        st.dataframe(
            collected_data.style.background_gradient(subset=['age'], cmap='Blues')
            .background_gradient(subset=['total_bilirubin'], cmap='Reds')
        )
        
        # Add download button
        csv = collected_data.to_csv(index=False)
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name="liver_prediction_data.csv",
            mime="text/csv"
        )
        
    else:
        st.info("Belum ada data yang terkumpul")

if __name__ == "__main__":
    show_evaluation()