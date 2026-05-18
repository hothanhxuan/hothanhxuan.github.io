import re

with open('d:\\PowerBI_Unigap\\portfolio\\projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_grid = """      <div class="projects-grid">
        <!-- Project 1 -->
        <div class="card project-card reveal" data-tags="python bigquery gcs">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary">Python</span>
            </div>
            <h3>Building an Omnichannel Retail Data Pipeline</h3>
            <p>A production-grade ETL pipeline processing <strong>6M+ records</strong> from multiple e-commerce platforms into a BigQuery Star Schema — with <strong>RFM customer segmentation</strong> and 3 Power BI dashboards.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">BigQuery</span>
              <span class="tag-outline">GCS</span>
              <span class="tag-outline">ETL Pipeline</span>
            </div>
            <a href="projects/etl-pipeline.html" class="project-link">View Case Study →</a>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">🛒</div>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="card project-card reveal" data-tags="powerbi">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary" style="background:#F59E0B">Power BI</span>
            </div>
            <h3>Strategic BI & Market Growth Dashboard — SuperStore Global</h3>
            <p>Comprehensive Power BI solution using a <strong>fact-dimension data model</strong> to process 51,000+ transaction records, tracking $12.64M revenue with 11.61% profit margin. Identified high-potential <strong>expansion zones</strong> like Canada.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">DAX</span>
              <span class="tag-outline">Data Modeling</span>
              <span class="tag-outline">Market Expansion</span>
            </div>
            <a href="projects/superstore-dashboard.html" class="project-link">View Case Study →</a>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">📈</div>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="card project-card reveal" data-tags="powerbi">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary" style="background:#F59E0B">Power BI</span>
            </div>
            <h3>HR Analytics: Employee Turnover & Workforce Performance</h3>
            <p>Analyzed data for ~300 employees tracking <strong>turnover rate</strong> (34.78%), average tenure (12.31 years), and engagement scores. Used DAX to pinpoint the Production department's 40.69% turnover and propose <strong>retention strategies</strong>.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">DAX</span>
              <span class="tag-outline">HR Metrics</span>
              <span class="tag-outline">Employee Retention</span>
            </div>
            <a href="projects/hr-analytics.html" class="project-link">View Case Study →</a>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">👥</div>
          </div>
        </div>

        <!-- Project 4 -->
        <div class="card project-card reveal" data-tags="powerbi">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary" style="background:#F59E0B">Power BI</span>
            </div>
            <h3>Marketing Spend & Sales Performance — Fashion Retail</h3>
            <p>Star Schema model integrating 10,500+ records across 4 tables with dynamic DAX measures for <strong>Week-over-Week ROAS</strong>, Budget, and Revenue Growth. Diagnosed underfunded hero SKUs and <strong>low-ROAS campaigns</strong>.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">DAX</span>
              <span class="tag-outline">ROAS Analysis</span>
              <span class="tag-outline">Marketing Analytics</span>
            </div>
            <a href="projects/fashion-marketing.html" class="project-link">View Case Study →</a>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">🛍️</div>
          </div>
        </div>

        <!-- Project 5 -->
        <div class="card project-card reveal" data-tags="powerbi">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary" style="background:#F59E0B">Power BI</span>
            </div>
            <h3>Flight Delays & Network Performance — US Aviation</h3>
            <p>Analytical dashboard processing <strong>5.8 million flight records</strong> across 322 airports and 14 airlines using a star-schema model. Analyzed <strong>On-Time Performance (OTP)</strong> and delay distributions to optimize flight schedules.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">Big Data</span>
              <span class="tag-outline">DAX</span>
              <span class="tag-outline">Network Operations</span>
            </div>
            <a href="projects/flight-delays.html" class="project-link">View Case Study →</a>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">✈️</div>
          </div>
        </div>

        <!-- Project 6 -->
        <div class="card project-card reveal" data-tags="sql bigquery">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary">SQL</span>
            </div>
            <h3>Unlocking User Behavior: Google Analytics Session Analysis</h3>
            <p>An Advanced SQL project utilizing <strong>Google BigQuery</strong> to analyze the public <strong>Google Analytics Sessions Dataset</strong>. The analysis leverages CTEs and data segmentation to uncover e-commerce conversion bottlenecks via <strong>Conversion Funnel Analysis</strong>, and contrasts <strong>Purchaser vs. Non-Purchaser Behavior</strong> to pinpoint engagement quality.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">BigQuery SQL</span>
              <span class="tag-outline">Funnel Analysis</span>
              <span class="tag-outline">User Segmentation</span>
            </div>
            <a href="projects/ecommerce-behavior.html" class="project-link">View Case Study →</a>
          </div>
          <div class="card-image" style="background: white;">
            <img src="assets/images/sql-ga-session/ga-session-cover-image.jpg" alt="Google Analytics Session Analysis" />
          </div>
        </div>

        <!-- Coming Soon 1 -->
        <div class="card project-card coming-soon reveal" data-tags="python ml">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary" style="background:#EC4899">Python / ML</span>
            </div>
            <h3>Machine Learning Project</h3>
            <p>Coming soon — stay tuned for an exciting machine learning project exploring predictive modeling and advanced analytics.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">Predictive Modeling</span>
              <span class="tag-outline">Scikit-Learn</span>
            </div>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">🤖</div>
          </div>
        </div>

        <!-- Coming Soon 2 -->
        <div class="card project-card coming-soon reveal" data-tags="sql">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary">SQL</span>
            </div>
            <h3>Advanced SQL Project</h3>
            <p>Coming soon — another deep-dive SQL analytics project focusing on complex business logic and performance tuning.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">Data Transformation</span>
              <span class="tag-outline">Window Functions</span>
            </div>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">📋</div>
          </div>
        </div>

        <!-- Coming Soon 3 -->
        <div class="card project-card coming-soon reveal" data-tags="excel">
          <div class="card-body">
            <div class="card-primary-tag">
              <span class="tag-primary" style="background:#22C55E">Excel</span>
            </div>
            <h3>Excel Analytics Project</h3>
            <p>Coming soon — showcasing advanced Excel capabilities, complex array formulas, and dynamic data wrangling skills.</p>
            <div class="card-secondary-tags">
              <span class="tag-outline">Power Query</span>
              <span class="tag-outline">Financial Modeling</span>
            </div>
          </div>
          <div class="card-image">
            <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; background:var(--bg-alt); font-size:4rem;">📊</div>
          </div>
        </div>
      </div>"""

updated_content = re.sub(r'<div class="projects-grid">.*</div>\n    </div>', new_grid + '\n    </div>', content, flags=re.DOTALL)

with open('d:\\PowerBI_Unigap\\portfolio\\projects.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)
