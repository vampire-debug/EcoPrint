import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EcoPrint",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# ENVIRONMENTAL FACTORS
# ============================================================

WATER_PER_SHEET = 7.0
CO2_PER_SHEET = 0.00464

# Approximate paper-to-tree conversion used only for
# educational visualization.
# Clearly presented as an estimate.
SHEETS_PER_TREE = 8333

# ============================================================
# FUNCTIONS
# ============================================================

def calculate_eco_score(
    print_type,
    colour,
    paper_size
):
    score = 50

    if print_type == "Double-sided":
        score += 30

    if colour == "Black & White":
        score += 10

    if paper_size == "A5":
        score += 10
    elif paper_size == "A4":
        score += 5

    return min(score, 100)


def calculate_sheets(
    pages,
    copies,
    print_type
):
    total_pages = pages * copies

    if print_type == "Double-sided":
        return total_pages, (total_pages + 1) // 2

    return total_pages, total_pages


# ============================================================
# HEADER
# ============================================================

st.title("🌱 EcoPrint")
st.subheader("Smart Printing & Paper Waste Analyzer")

st.write(
    "Analyze printing habits, estimate environmental impact, "
    "identify paper waste, and discover sustainable printing "
    "opportunities."
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🌱 EcoPrint")

st.sidebar.write(
    "Smart Printing & Paper Waste Analyzer"
)

page = st.sidebar.radio(
    "Navigate",
    [
        "🖨️ Print Calculator",
        "📊 Dataset Analyzer",
        "🌍 Sustainability Dashboard"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Green Computing Project"
)

# ============================================================
# SESSION STATE
# ============================================================

if "analysis_df" not in st.session_state:
    st.session_state.analysis_df = None


# ============================================================
# PAGE 1 — PRINT CALCULATOR
# ============================================================

if page == "🖨️ Print Calculator":

    st.header("📝 Enter Printing Details")

    col1, col2 = st.columns(2)

    with col1:

        pages = st.number_input(
            "Number of pages",
            min_value=1,
            value=100,
            step=1
        )

        copies = st.number_input(
            "Number of copies",
            min_value=1,
            value=1,
            step=1
        )

        print_type = st.selectbox(
            "Current printing method",
            [
                "Single-sided",
                "Double-sided"
            ]
        )

    with col2:

        paper_size = st.selectbox(
            "Paper size",
            [
                "A4",
                "A3",
                "A5"
            ]
        )

        colour = st.selectbox(
            "Print mode",
            [
                "Black & White",
                "Colour"
            ]
        )

        paper_cost = st.number_input(
            "Cost per sheet (₹)",
            min_value=0.1,
            value=1.0,
            step=0.1
        )

    if st.button(
        "🔍 Analyze Printing Impact",
        use_container_width=True
    ):

        total_pages, current_sheets = calculate_sheets(
            pages,
            copies,
            print_type
        )

        single_sided_sheets = total_pages

        double_sided_sheets = (
            total_pages + 1
        ) // 2

        # Current environmental impact

        current_water = (
            current_sheets *
            WATER_PER_SHEET
        )

        current_co2 = (
            current_sheets *
            CO2_PER_SHEET
        )

        current_cost = (
            current_sheets *
            paper_cost
        )

        # Double-sided alternative

        eco_water = (
            double_sided_sheets *
            WATER_PER_SHEET
        )

        eco_co2 = (
            double_sided_sheets *
            CO2_PER_SHEET
        )

        eco_cost = (
            double_sided_sheets *
            paper_cost
        )

        # Potential savings

        paper_saved = (
            single_sided_sheets -
            double_sided_sheets
        )

        water_saved = (
            paper_saved *
            WATER_PER_SHEET
        )

        co2_saved = (
            paper_saved *
            CO2_PER_SHEET
        )

        money_saved = (
            paper_saved *
            paper_cost
        )

        eco_score = calculate_eco_score(
            print_type,
            colour,
            paper_size
        )

        # Store calculator results

        st.session_state.calculator_results = {
            "total_pages": total_pages,
            "current_sheets": current_sheets,
            "paper_saved": paper_saved,
            "water_saved": water_saved,
            "co2_saved": co2_saved,
            "money_saved": money_saved,
            "eco_score": eco_score
        }

        # ====================================================
        # RESULTS
        # ====================================================

        st.divider()

        st.header("📊 Your Environmental Impact")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "📄 Paper Used",
            f"{current_sheets} sheets"
        )

        c2.metric(
            "💧 Water Impact",
            f"{current_water:.1f} L"
        )

        c3.metric(
            "🌍 CO₂ Impact",
            f"{current_co2:.2f} kg"
        )

        c4.metric(
            "💰 Estimated Cost",
            f"₹{current_cost:.2f}"
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🌱 Eco Score",
            f"{eco_score}/100"
        )

        c2.metric(
            "📑 Total Pages",
            total_pages
        )

        c3.metric(
            "🖨️ Print Mode",
            print_type
        )

        c4.metric(
            "📐 Paper Size",
            paper_size
        )

        # ====================================================
        # COMPARISON
        # ====================================================

        st.divider()

        st.header("♻️ Single-Sided vs Double-Sided")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📄 Single-Sided")

            st.write(
                f"Sheets: **{single_sided_sheets}**"
            )

            st.write(
                f"Water: **"
                f"{single_sided_sheets * WATER_PER_SHEET:.1f} L**"
            )

            st.write(
                f"CO₂: **"
                f"{single_sided_sheets * CO2_PER_SHEET:.2f} kg**"
            )

            st.write(
                f"Cost: **₹"
                f"{single_sided_sheets * paper_cost:.2f}**"
            )

        with col2:

            st.subheader("🌱 Double-Sided")

            st.write(
                f"Sheets: **{double_sided_sheets}**"
            )

            st.write(
                f"Water: **{eco_water:.1f} L**"
            )

            st.write(
                f"CO₂: **{eco_co2:.2f} kg**"
            )

            st.write(
                f"Cost: **₹{eco_cost:.2f}**"
            )

        # ====================================================
        # SAVINGS
        # ====================================================

        st.divider()

        st.header("💚 Potential Savings")

        s1, s2, s3, s4 = st.columns(4)

        s1.metric(
            "📄 Paper Saved",
            f"{paper_saved} sheets"
        )

        s2.metric(
            "💧 Water Saved",
            f"{water_saved:.1f} L"
        )

        s3.metric(
            "🌍 CO₂ Reduced",
            f"{co2_saved:.2f} kg"
        )

        s4.metric(
            "💰 Money Saved",
            f"₹{money_saved:.2f}"
        )

        # ====================================================
        # CHART
        # ====================================================

        st.divider()

        st.header("📈 Paper Usage Comparison")

        chart_data = pd.DataFrame({
            "Printing Method": [
                "Single-Sided",
                "Double-Sided"
            ],
            "Paper Sheets": [
                single_sided_sheets,
                double_sided_sheets
            ]
        })

        fig = px.bar(
            chart_data,
            x="Printing Method",
            y="Paper Sheets",
            text="Paper Sheets",
            title="Paper Consumption Comparison"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ====================================================
        # RECOMMENDATIONS
        # ====================================================

        st.divider()

        st.header("💡 Smart Recommendations")

        if print_type == "Single-sided":

            st.warning(
                "♻️ Switch to double-sided printing. "
                f"You could save approximately "
                f"{paper_saved} sheets."
            )

        else:

            st.success(
                "✅ Great! You are already using "
                "double-sided printing."
            )

        if colour == "Colour":

            st.info(
                "🖨️ Consider Black & White printing "
                "when colour is not necessary."
            )

        else:

            st.success(
                "✅ Black & White printing helps "
                "reduce colour ink/toner consumption."
            )

        if copies > 5:

            st.info(
                "📑 You are printing multiple copies. "
                "Consider digital sharing where possible."
            )

        if eco_score >= 80:

            st.success(
                f"🌱 Excellent! Your Eco Score is "
                f"{eco_score}/100."
            )

        elif eco_score >= 60:

            st.info(
                f"🌿 Good start! Your Eco Score is "
                f"{eco_score}/100."
            )

        else:

            st.warning(
                f"⚠️ Your Eco Score is "
                f"{eco_score}/100."
            )


# ============================================================
# PAGE 2 — DATASET ANALYZER
# ============================================================

elif page == "📊 Dataset Analyzer":

    st.header("📊 Printing Dataset Analyzer")

    st.write(
        "Upload a CSV file containing multiple printing "
        "records to analyze paper consumption and "
        "environmental impact."
    )

    st.info(
        "Required columns: Date, Pages, Copies, "
        "Print_Type, Colour, Paper_Cost"
    )

    # --------------------------------------------------------
    # SAMPLE DATA
    # --------------------------------------------------------

    sample_data = pd.DataFrame({
        "Date": [
            "2026-10-01",
            "2026-10-02",
            "2026-10-03",
            "2026-10-04",
            "2026-10-05"
        ],
        "Pages": [
            50,
            100,
            200,
            75,
            150
        ],
        "Copies": [
            1,
            2,
            1,
            3,
            1
        ],
        "Print_Type": [
            "Single-sided",
            "Double-sided",
            "Single-sided",
            "Double-sided",
            "Single-sided"
        ],
        "Colour": [
            "Colour",
            "Black & White",
            "Black & White",
            "Black & White",
            "Colour"
        ],
        "Paper_Cost": [
            1,
            1,
            1,
            1,
            1
        ]
    })

    st.download_button(
        "📥 Download Sample CSV",
        sample_data.to_csv(index=False),
        "ecoprint_sample_data.csv",
        "text/csv"
    )

    uploaded_file = st.file_uploader(
        "📂 Upload your printing CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(
                uploaded_file
            )

            required_columns = [
                "Date",
                "Pages",
                "Copies",
                "Print_Type",
                "Colour",
                "Paper_Cost"
            ]

            missing_columns = [
                col
                for col in required_columns
                if col not in df.columns
            ]

            if missing_columns:

                st.error(
                    "❌ Missing columns: "
                    + ", ".join(missing_columns)
                )

                st.stop()

            # ------------------------------------------------
            # CLEAN DATA
            # ------------------------------------------------

            df["Date"] = pd.to_datetime(
                df["Date"],
                errors="coerce"
            )

            df["Pages"] = pd.to_numeric(
                df["Pages"],
                errors="coerce"
            )

            df["Copies"] = pd.to_numeric(
                df["Copies"],
                errors="coerce"
            )

            df["Paper_Cost"] = pd.to_numeric(
                df["Paper_Cost"],
                errors="coerce"
            )

            df = df.dropna(
                subset=[
                    "Date",
                    "Pages",
                    "Copies",
                    "Print_Type",
                    "Paper_Cost"
                ]
            )

            if df.empty:

                st.error(
                    "❌ No valid records found."
                )

                st.stop()

            # ------------------------------------------------
            # CALCULATIONS
            # ------------------------------------------------

            df["Total_Pages"] = (
                df["Pages"] *
                df["Copies"]
            )

            df["Sheets_Used"] = df.apply(
                lambda row:
                (
                    (int(row["Total_Pages"]) + 1) // 2
                    if row["Print_Type"]
                    == "Double-sided"
                    else int(row["Total_Pages"])
                ),
                axis=1
            )

            df["Water_Litres"] = (
                df["Sheets_Used"] *
                WATER_PER_SHEET
            )

            df["CO2_kg"] = (
                df["Sheets_Used"] *
                CO2_PER_SHEET
            )

            df["Printing_Cost"] = (
                df["Sheets_Used"] *
                df["Paper_Cost"]
            )

            df["Double_Sided_Sheets"] = (
                (df["Total_Pages"] + 1) // 2
            )

            df["Potential_Paper_Saving"] = (
                df["Sheets_Used"] -
                df["Double_Sided_Sheets"]
            )

            df["Potential_Water_Saving"] = (
                df["Potential_Paper_Saving"] *
                WATER_PER_SHEET
            )

            df["Potential_CO2_Reduction"] = (
                df["Potential_Paper_Saving"] *
                CO2_PER_SHEET
            )

            # Store in session state

            st.session_state.analysis_df = df

            st.success(
                "✅ Dataset analyzed successfully!"
            )

            # ------------------------------------------------
            # SUMMARY
            # ------------------------------------------------

            st.divider()

            st.header("📊 Dataset Summary")

            total_pages = int(
                df["Total_Pages"].sum()
            )

            total_sheets = int(
                df["Sheets_Used"].sum()
            )

            total_water = (
                df["Water_Litres"].sum()
            )

            total_co2 = (
                df["CO2_kg"].sum()
            )

            total_cost = (
                df["Printing_Cost"].sum()
            )

            potential_savings = int(
                df["Potential_Paper_Saving"].sum()
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "📑 Total Pages",
                f"{total_pages:,}"
            )

            c2.metric(
                "📄 Sheets Used",
                f"{total_sheets:,}"
            )

            c3.metric(
                "💧 Water Impact",
                f"{total_water:,.1f} L"
            )

            c4.metric(
                "🌍 CO₂ Impact",
                f"{total_co2:,.2f} kg"
            )

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "💰 Printing Cost",
                f"₹{total_cost:,.2f}"
            )

            c2.metric(
                "♻️ Potential Paper Saving",
                f"{potential_savings:,} sheets"
            )

            c3.metric(
                "💧 Potential Water Saving",
                f"{potential_savings * WATER_PER_SHEET:,.1f} L"
            )

            c4.metric(
                "🌍 Potential CO₂ Reduction",
                f"{potential_savings * CO2_PER_SHEET:,.2f} kg"
            )

            # ------------------------------------------------
            # DATA TABLE
            # ------------------------------------------------

            st.divider()

            st.header("📋 Processed Dataset")

            st.dataframe(
                df,
                use_container_width=True
            )

            # ------------------------------------------------
            # DAILY TREND
            # ------------------------------------------------

            st.divider()

            st.header("📈 Printing Trend")

            daily_data = (
                df.groupby("Date")["Sheets_Used"]
                .sum()
                .reset_index()
            )

            fig = px.line(
                daily_data,
                x="Date",
                y="Sheets_Used",
                markers=True,
                title="Daily Paper Consumption"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ------------------------------------------------
            # PRINTING METHOD
            # ------------------------------------------------

            st.header("♻️ Printing Method Analysis")

            method_data = (
                df.groupby("Print_Type")["Sheets_Used"]
                .sum()
                .reset_index()
            )

            fig2 = px.bar(
                method_data,
                x="Print_Type",
                y="Sheets_Used",
                text="Sheets_Used",
                title="Paper Consumption by Printing Method"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

            # ------------------------------------------------
            # COLOUR ANALYSIS
            # ------------------------------------------------

            st.header("🖨️ Colour vs Black & White")

            colour_data = (
                df.groupby("Colour")["Sheets_Used"]
                .sum()
                .reset_index()
            )

            fig3 = px.pie(
                colour_data,
                names="Colour",
                values="Sheets_Used",
                title="Printing Mode Distribution"
            )

            st.plotly_chart(
                fig3,
                use_container_width=True
            )

            # ------------------------------------------------
            # DOWNLOAD
            # ------------------------------------------------

            st.divider()

            st.header("📥 Download Analysis")

            st.download_button(
                "⬇️ Download Processed Dataset",
                df.to_csv(index=False),
                "ecoprint_analysis.csv",
                "text/csv"
            )

        except Exception as e:

            st.error(
                f"❌ Unable to process the dataset: {e}"
            )


# ============================================================
# PAGE 3 — SUSTAINABILITY DASHBOARD
# ============================================================

elif page == "🌍 Sustainability Dashboard":

    st.header("🌍 EcoPrint Sustainability Dashboard")

    st.write(
        "A summary of the environmental savings that can be "
        "achieved by adopting sustainable printing practices."
    )

    # ========================================================
    # DATA SOURCE
    # ========================================================

    df = st.session_state.analysis_df

    if df is None:

        st.warning(
            "⚠️ No dataset has been analyzed yet."
        )

        st.info(
            "Go to **📊 Dataset Analyzer**, upload a CSV, "
            "and then return to this dashboard."
        )

        st.stop()

    # ========================================================
    # TOTAL VALUES
    # ========================================================

    total_pages = int(
        df["Total_Pages"].sum()
    )

    total_sheets = int(
        df["Sheets_Used"].sum()
    )

    total_water = (
        df["Water_Litres"].sum()
    )

    total_co2 = (
        df["CO2_kg"].sum()
    )

    total_cost = (
        df["Printing_Cost"].sum()
    )

    paper_saved = int(
        df["Potential_Paper_Saving"].sum()
    )

    water_saved = (
        paper_saved *
        WATER_PER_SHEET
    )

    co2_saved = (
        paper_saved *
        CO2_PER_SHEET
    )

    money_saved = (
        df["Potential_Paper_Saving"] *
        df["Paper_Cost"]
    ).sum()

    # ========================================================
    # SUSTAINABILITY METRICS
    # ========================================================

    tree_equivalent = (
        paper_saved /
        SHEETS_PER_TREE
    )

    # Overall sustainability score

    double_sided_records = (
        df["Print_Type"]
        .eq("Double-sided")
        .sum()
    )

    total_records = len(df)

    if total_records > 0:

        double_sided_percentage = (
            double_sided_records /
            total_records
        ) * 100

    else:

        double_sided_percentage = 0

    sustainability_score = min(
        100,
        round(
            50 +
            (double_sided_percentage * 0.4)
        )
    )

    # ========================================================
    # MAIN DASHBOARD
    # ========================================================

    st.divider()

    st.subheader("🌱 Environmental Savings")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📄 Paper Potentially Saved",
        f"{paper_saved:,} sheets"
    )

    c2.metric(
        "💧 Water Potentially Saved",
        f"{water_saved:,.1f} L"
    )

    c3.metric(
        "🌍 CO₂ Potentially Reduced",
        f"{co2_saved:,.2f} kg"
    )

    c4.metric(
        "💰 Potential Cost Saving",
        f"₹{money_saved:,.2f}"
    )

    # ========================================================
    # SECONDARY METRICS
    # ========================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📑 Total Pages",
        f"{total_pages:,}"
    )

    c2.metric(
        "📄 Current Sheets",
        f"{total_sheets:,}"
    )

    c3.metric(
        "🌳 Tree Equivalent",
        f"{tree_equivalent:.2f}"
    )

    c4.metric(
        "🌱 Sustainability Score",
        f"{sustainability_score}/100"
    )

    # ========================================================
    # PROGRESS BAR
    # ========================================================

    st.divider()

    st.subheader("🌱 Sustainability Score")

    st.progress(
        sustainability_score / 100
    )

    if sustainability_score >= 80:

        st.success(
            "🌿 Excellent sustainable printing practices!"
        )

    elif sustainability_score >= 60:

        st.info(
            "🌱 Good progress. There is still room "
            "for improvement."
        )

    else:

        st.warning(
            "⚠️ Printing practices can be improved "
            "by increasing double-sided printing."
        )

    # ========================================================
    # SAVINGS CHART
    # ========================================================

    st.divider()

    st.subheader("📊 Potential Environmental Savings")

    savings_data = pd.DataFrame({
        "Environmental Metric": [
            "Paper Saved",
            "Water Saved",
            "CO₂ Reduced"
        ],
        "Value": [
            paper_saved,
            water_saved,
            co2_saved
        ]
    })

    fig = px.bar(
        savings_data,
        x="Environmental Metric",
        y="Value",
        text="Value",
        title="Potential Environmental Savings"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ========================================================
    # PRINTING PRACTICE
    # ========================================================

    st.divider()

    st.subheader("♻️ Printing Practice")

    practice_data = pd.DataFrame({
        "Printing Method": [
            "Single-sided",
            "Double-sided"
        ],
        "Records": [
            (
                df["Print_Type"]
                .eq("Single-sided")
                .sum()
            ),
            (
                df["Print_Type"]
                .eq("Double-sided")
                .sum()
            )
        ]
    })

    fig2 = px.pie(
        practice_data,
        names="Printing Method",
        values="Records",
        title="Printing Method Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ========================================================
    # INSIGHTS
    # ========================================================

    st.divider()

    st.subheader("💡 Sustainability Insights")

    if double_sided_percentage < 50:

        st.warning(
            f"♻️ Only {double_sided_percentage:.1f}% "
            "of printing records use double-sided printing. "
            "Increasing this can significantly reduce paper use."
        )

    else:

        st.success(
            f"✅ {double_sided_percentage:.1f}% of your "
            "printing records use double-sided printing."
        )

    if paper_saved > 0:

        st.success(
            f"🌱 Switching eligible printing jobs to "
            f"double-sided could save approximately "
            f"{paper_saved:,} sheets."
        )

    if tree_equivalent > 0:

        st.info(
            f"🌳 The potential paper saving is equivalent "
            f"to approximately {tree_equivalent:.2f} "
            "tree's worth of paper."
        )

    # ========================================================
    # METHODOLOGY
    # ========================================================

    st.divider()

    with st.expander("📚 Calculation Methodology"):

        st.write(
            f"""
            **Water footprint:** {WATER_PER_SHEET} litres per sheet

            **CO₂ footprint:** {CO2_PER_SHEET * 1000:.2f} grams CO₂e per sheet

            **Tree equivalent:** approximately one tree per
            {SHEETS_PER_TREE:,} sheets for educational estimation.

            Environmental values are approximate estimates and
            can vary based on paper type, manufacturing process,
            recycling rate and location.
            """
        )

    # ========================================================
    # FOOTER
    # ========================================================

    st.divider()

    st.caption(
        "EcoPrint | Green Computing Project | "
        "Smart Printing & Paper Waste Analyzer"
    )