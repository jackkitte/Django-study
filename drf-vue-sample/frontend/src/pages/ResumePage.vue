<template>
  <div id="resume-page">
    <GlobalHeader/>
    <GlobalMessage/>

    <main class="container my-5">
      <b-row>
        <b-col cols=12 class="text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ resume.companyName }}</h2>
        </b-col>
        <b-col md=3 class="mb-4">
          <b-img
            class="img-fluid"
            style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
            :src="resume.picture"
            alt
          ></b-img>
        </b-col>
        <b-col md=9>
          <div class="resume-details">
            <b-row>
              <b-col>
                <h4>プロジェクト</h4>
                <p>{{ resume.project }}</p>
              </b-col>
              <b-col>
                <h4>プロジェクト期間</h4>
                <p>{{ resume.term }}</p>
              </b-col>
            </b-row>
            <h4>プロジェクト概要</h4>
            <textarea class="form-control" rows="10" v-html="resume.overview" disabled />
            <br>
            <h4>開発環境</h4>
            <textarea class="form-control" rows="10" v-html="resume.develop" disabled />
          </div>
        </b-col>
      </b-row>
    </main>
  </div>
</template>

<script>
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalMessage from '@/components/GlobalMessage.vue'

const sampleData = [
  {
    id: 1,
    companyName: "株式会社ウェザーニューズ",
    picture: require("@/assets/lambda.png"),
    project: "LINE防災チャットボット研究開発",
    term: "2018年8月 ~ 現在",
    overview: `メッセージングツール（LINEなど）の活用による、国民一人ひとりへの避難支援を実現するシステムの開発
・被災通報などを通して国民一人ひとりの社会動態/被災状況把握を行い、政府の災害対応における「情報収集の効率化/省力化」それに伴う「意思決定の高度化/迅速化」
・国民一人ひとりに対して最適化された情報の伝達を半自動的に行う仕組みによる「被災者支援の高度化/効率化」

[研究体制]
自然言語専門の上司のもと、初期プロトタイプの設計/実装を担当。より汎用化を目指して、開発メンバーを増員し、上司と開発メンバーとの橋渡し的な役割を行いつつ、開発に従事中。開発スタイルはスクラム開発。

[課題]
災害時、従来は電話などを通して大量の個別要望などが寄せられていたが、圧倒的な人的資源の不足により、適切な対処が実現できていませんでした。

[課題に対するアプローチ]
上記の課題に対して、所謂チャットボットというシステムを導入することで、人的資源が不足する災害対応機関業務の自動化、効率化に貢献する。

[成果]
初期プロトタイプを実際の自治体の避難訓練で試験運用することで、災害時の社会動態情報の収集や避難などに資する情報を個人に伝達する手段の確立とアナログによる情報収集/伝達に対する優位性が確認できた。`,
    develop: `チャットボットの主要部分はAPI Gateway/SQS/Lambda/DynamoDBの構成で開発
チャットボットからユーザーへのPush通知機能のバックエンドはAPI Gateway/VPC/Lambda/Aurora PostgreSQLの構成で開発。フロントエンド部分はNuxt.jsで開発、現在はReactへの移行を検討中
ソースコードはGitHubで管理し、CodePipeline/ECR/GitHub/CodeBuildの構成でデプロイを行います。
開発チームではSlackを使ったコミュニケーション、Jira/confluenceを使用したプロジェクト管理で動いています。`,
  },
  {
    id: 2,
    companyName: "株式会社つうけんアドバンスシステムズ",
    picture: require("@/assets/nodejs.png"),
    project: "チャットボット導入検討",
    term: "2018年1月 ~ 2018年7月",
    overview: `オペレーションセンターの業務効率化を測るためのchatbotシステムの検証を行っております。当初の取り組みとしては、Jumanを用いて形態素解析したテキストデータをknpに入力することで構文解析を行います。構文解析を行うことで、問合せ内容の文脈の意図を推定することができ、問合せに対応した回答を返すことができるようになります。例えば「Office365とは何ですか？」、「Office365の利用方法は何ですか？」の場合ですと、前者はOffice365自体についての概要が知りたいという意図が推定でき、後者はOffice365の導入方法や使い方、利用に必要な環境などが知りたいという意図が推定できます。

[アプローチ]
また、オープソースとして「bot-express」というものがあります。概要としては「bot-expressはオーダーメイドのChatbotを高速に開発するためのフレームワークでNode.jsで動作します。開発者はフォーマットにしたがって「スキル」を追加するだけでChatbotの能力を拡張していくことができます。」とあり、chatbotシステムをこのフレームワークを使って実装できないか検証も行っております。
スキルの部分が所謂「シナリオ」のことであり、「この問合せが来たらこの回答をする」という処理が書かれております。このスキルが問合せの意図毎に複数あります。そして、問合せの意図を判断するのがNLU(自然言語理解)になります。bot-expressではNLUにDialogflow(google)を用いています。将来的には、このNLU部分をPythonとJumann++とknpを使った構文解析などによって、内製していきたいとも考えております。`,
    develop: `自然言語処理/Bot開発周りの知見を有しているものがおりませんので、情報収集から開発まですべて一人で行っております。`
  },
  {
    id: 3,
    companyName: "株式会社つうけんアドバンスシステムズ",
    picture: require("@/assets/elasticstack.png"),
    project: "検索エンジンシステムの検証",
    term: "2018年1月 ~ 2018年7月",
    overview: `オペレーションセンターに蓄積されたテキストデータ(ナレッジ情報)の有効活用として、自然言語解析を行っておりましたが、別のアプローチとして、ナレッジ検索システムを構築すれば良いのではと考え、Elasticsearchを用いた検索システムの検証を行っております。

[課題]
そもそもの課題として、ナレッジ情報が整理されていないという問題があります。そのため、ナレッジ情報の探索が難しい現状です。簡単な検索システムを導入するだけでも、業務効率化が図れると考え、検索システムの導入を提案し、検証を行っております。

[課題に対するアプローチ]
検索エンジンとしては、Elasticsearchを用いております。Elasticsearchは、構造型、非構造型、地理情報、メトリックなど多様なデータタイプに対応した検索/分析ができます。うちの部署としては、社内のナレッジ情報を自然言語解析しており、今後は、社内で運用管理しているシステムから出るメトリクスデータ解析も行うのでElasticsearchを検索/分析に使うのは適切と考えました。
また、データ検索/分析結果をWebベースで可視化するツールとして、Kibanaがあります。こちらは、Elasticsearchと同じ会社が作っており、とても親和性が高く、非常に導入が簡単であり、最初の検証ツールとしては良いと考えElasticsearchとKibanaを使った検索エンジン基盤を構築しております。

[成果]
Elasticsearchによる検索エンジンの導入のしやすさ、また、分析基盤としての高い有用性、BeatsやLogstashのETLとしての機能の豊富さ、Kibanaのダッシュボードとしての便利さ等、検索エンジン以上の知見を得られました。`,
    develop: `検索エンジン周りについての知見を有しているものがいないので、検索エンジンに関する技術情報の収集から選定/導入/構築/検証に至るまで私一人で行っております。`
  }
];

export default {
  head() {
    return {
      title: "View Resume"
    };
  },
  components: {
    GlobalHeader,
    GlobalMessage
  },
  created: function () {
    let data = sampleData;
    let id = this.$route.params.resumeId;
    this.resume = data[id - 1]
  },
  data() {
    return {
      resume: {
        name: "",
        picture: "",
        ingredients: "",
        difficulty: "",
        prep_time: null,
        prep_guide: ""
      }
    };
  }
};
</script>

<style scoped>
</style>
