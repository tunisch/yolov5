import matplotlib.pyplot as plt
import pandas as pd

def plot_results(results_file):
    """
    Plots training and validation metrics from the results CSV file.
    Args:
        results_file (str): Path to the results CSV file generated during training.
    """
    # Load results from CSV
    df = pd.read_csv(results_file, delimiter=',')  # CSV dosyasını oku

    # Clean column names by removing extra spaces
    df.columns = df.columns.str.strip()

    # Extract metrics
    epoch = df['epoch']
    train_loss = df['train/box_loss']
    val_loss = df['val/box_loss']
    precision = df['metrics/precision']
    recall = df['metrics/recall']
    mAP = df['metrics/mAP_0.5']

    # Plot losses
    plt.figure(figsize=(10, 5))
    plt.plot(epoch, train_loss, label='Train Loss')
    plt.plot(epoch, val_loss, label='Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.show()

    # Plot precision, recall, and mAP
    plt.figure(figsize=(10, 5))
    plt.plot(epoch, precision, label='Precision')
    plt.plot(epoch, recall, label='Recall')
    plt.plot(epoch, mAP, label='mAP@0.5')
    plt.xlabel('Epochs')
    plt.ylabel('Metrics')
    plt.title('Precision, Recall, and mAP@0.5')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    results_file = "runs/train/exp/results.csv"  # Update this path if needed
    plot_results(results_file)