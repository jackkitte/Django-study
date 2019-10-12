<template>
  <div id="profile-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <!-- メインエリア -->
    <main class="container" id="profile">
      <p class="h5 mb-4">プロフィール</p>
      <b-row>
        <b-col>
          <b-card border-variant="secondary" bg-variant="info" text-variant="white" class="mb-2">
            <b-row no-gutters>
              <b-col md=3>
                <!-- <b-card-img src="https://i.imgur.com/rNRG0gR.png" class="rounded-0"></b-card-img> -->
                <b-card-img src="../assets/ponkue_kaku.jpeg" class="rounded-0"></b-card-img>
              </b-col>
              <b-col md=9>
                <b-card-body title="玉城 翔（たましろ　かける）">
                  <b-row>
                    <b-col>年齢：</b-col><b-col>29</b-col>
                  </b-row>
                  <b-row>
                    <b-col>性別：</b-col><b-col>男</b-col>
                  </b-row>
                  <b-row>
                    <b-col>出身地：</b-col><b-col>沖縄</b-col>
                  </b-row>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
          <b-card header-bg-variant="primary" header-text-variant="white" class="mb-2">
            <template v-slot:header>
              <h5 class="mb-0">学　歴</h5>
            </template>
            <b-row>
              <b-col md=3>2013年 3月</b-col>
              <b-col md=9>琉球大学　工学部　情報工学科</b-col>
            </b-row>
            <b-row>
              <b-col md=3>2015年 5月</b-col>
              <b-col md=9>琉球大学大学院　理工学研究科　情報工学専攻</b-col>
            </b-row>
            <br>
            <b-card-text>
              　大学で情報工学を学び、研究では當間研究室にてニューラルネットワークをやっておりました。ディープラーニングにおけるパラメータ調整を自動で最適な値に設定できないかどうかの検証を行いました。
            </b-card-text>
          </b-card>
          <b-card header-bg-variant="secondary" header-text-variant="white" class="overflow-hidden">
            <template v-slot:header>
              <h5 class="mb-0">来　歴</h5>
            </template>
            <b-row>
              <b-col md=3>2015年 4月~2015 12月</b-col>
              <b-col md=8>
                <p>株式会社UBIC　新卒入社</p>
                <p>上級研究員の支持のもと、最新論文や技術を調査し、それらの技術が人工知能エンジンに適用可能かどうかの簡易なテストも含めた調査報告を行っていた。</p>
              </b-col>
            </b-row>
            <b-row>
              <b-col md=3>2017年 5月~2018年 7月</b-col>
              <b-col md=9>
                <p>株式会社つうけんアドバンスシステムズ　中途入社</p>
                <p>社内の業務効率化のための様々な技術検証を行っていました。テキストマイニング、Elasticsearchを用いた検索システムの検証、GoogleAnalyticsを使ったWeb解析、Node.js製のチャットボットフレームワークの導入検討など。</p>
              </b-col>
            </b-row>
            <b-row>
              <b-col md=3>2018年 8月~現在</b-col>
              <b-col md=9>
                <p>株式会社ウェザーニューズ　中途入社</p>
                <p>LINEチャットボットを活用した、国民一人ひとりへの避難支援を実現するシステムの開発</p>
              </b-col>
            </b-row>
          </b-card>
        </b-col>
        <b-col>
          <b-card header-bg-variant="danger" header-text-variant="white" class="overflow-hidden">
            <template v-slot:header>
              <h5 class="mb-0">スキルセット</h5>
            </template>
            <b-card-text>プログラミング</b-card-text>
            <div class="ml-3">
              <b-badge variant="danger" class="mr-1">Python3 5年以上</b-badge>
              <b-badge variant="warning" class="mr-1">JavaScript 3~5年</b-badge>
              <b-badge variant="primary" class="mr-1">SQL 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">Bash 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">ES6 1年未満</b-badge>
            </div>
            <br>
            <b-card-text>アプリケーションフレームワーク</b-card-text>
            <div class="ml-3">
              <b-badge variant="success" class="mr-1">Django 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">Vue.js 1~3年</b-badge>
              <b-badge variant="primary" class="mr-1">django-rest-framework 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">Nuxt.js 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">React 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">Node.js 1年未満</b-badge>
            </div>
            <br>
            <b-card-text>AWS</b-card-text>
            <div class="ml-3">
              <b-badge variant="success" class="mr-1">Lambda 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">DynamoDB 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">API Gateway 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">SQS 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">Aurora PostgreSQL 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">VPC 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">S3 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">CloudWatch 1~3年</b-badge>
              <b-badge variant="primary" class="mr-1">Kinesis 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">Events 1年未満</b-badge>
            </div>
            <br>
            <b-card-text>DevOps</b-card-text>
            <div class="ml-3">
              <b-badge variant="danger" class="mr-1">macOS 5年以上</b-badge>
              <b-badge variant="warning" class="mr-1">Linux 3~5年</b-badge>
              <b-badge variant="warning" class="mr-1">Git 3~5年</b-badge>
              <b-badge variant="warning" class="mr-1">GitHub 3~5年</b-badge>
              <b-badge variant="success" class="mr-1">pytest 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">Docker 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">AWS SAM 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">AWS CloudFormation 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">AWS CodeBuild 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">AWS CodePipeline 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">AWS ECR 1~3年</b-badge>
              <b-badge variant="primary" class="mr-1">Heroku 1年未満</b-badge>
            </div>
            <br>
            <b-card-text>チーム開発ツール</b-card-text>
            <div class="ml-3">
              <b-badge variant="warning" class="mr-1">slack 3~5年</b-badge>
              <b-badge variant="success" class="mr-1">VSCode 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">アジャイル開発 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">Jira 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">Confluence 1~3年</b-badge>
            </div>
            <br>
            <b-card-text>データ分析</b-card-text>
            <div class="ml-3">
              <b-badge variant="success" class="mr-1">scikit-learn 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">MeCab 1~3年</b-badge>
              <b-badge variant="success" class="mr-1">gensim 1~3年</b-badge>
              <b-badge variant="primary" class="mr-1">JupyterNotebook 1年未満</b-badge>
              <b-badge variant="primary" class="mr-1">ElasticStack 1年未満</b-badge>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </main>
  </div>
</template>

<script>
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalMessage from '@/components/GlobalMessage.vue'
export default {
  components: {
    GlobalHeader,
    GlobalMessage,
  }
}
</script>
