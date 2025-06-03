ARG PYTHON_IMAGE_TAG
FROM python:$PYTHON_IMAGE_TAG

# パッケージ更新
RUN apt-get update
# 追加で必要な時は apt-get install ... OR 改行で欲しいものを追加

# パラメータ変数
ARG USERNAME
ARG GROUPNAME
ARG UID
ARG GID
ARG WORKDIR

# importの指定がディレクトリからになるためラク
ENV PYTHONPATH $WORKDIR

# ユーザー追加
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID $USERNAME && \
    mkdir -p $WORKDIR && \
    chown -R $UID:$GID $WORKDIR

# ユーザーのbinaryディレクトリをパスに追加
ENV PATH /home/$USERNAME/.local/bin:$PATH

# ユーザー切り替え
USER $USERNAME

# 作業ディレクトリ設定
WORKDIR $WORKDIR

# パッケージ更新
RUN python -m pip install --upgrade --user pip
RUN python -m pip install --upgrade --user setuptools

# パッケージインストール（requirements.txtから）
COPY requirements.txt $WORKDIR
RUN python -m pip install --user -r requirements.txt
