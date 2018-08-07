// gulpプラグインの読み込み
const gulp = require('gulp');
// Sassをコンパイルするプラグインの読み込み
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');

// style.scssをタスクを作成する
gulp.task('default', function () {
    // scssフォルダを監視し、変更があったらコンパイルする
    gulp.watch('scss/*.scss', function() {
        // style.scssファイルを取得
        gulp.src('Adviser/static/Adviser/css/stylesheets/style.scss')
        // Sassのコンパイルを実行
        .pipe(sass())
        // ベンダープレフィックスの付与
        .pipe(autoprefixer())
        // cssフォルダー以下に保存
        .pipe(gulp.dest('Adviser/static/Adviser/css'));
    });
});
