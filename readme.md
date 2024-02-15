# commands I used

training (i dont have a strong external gpu)
took about an hour or sumn
```
python train.py config/train_tweets.py --device=cpu --compile=False --eval_iters=60 --log_interval=1 --block_size=128 --batch_size=32 --n_layer=8 --n_head=8 --n_embd=128 --max_iters=5000 --lr_decay_iters=3500 --dropout=0.0
```

generate output
```
python sample.py --out_dir=out_tweets --device=cpu
```