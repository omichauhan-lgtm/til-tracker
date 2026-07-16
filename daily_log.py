import os
import random
from datetime import datetime

# A rich database of actual systems engineering, data pipeline, and DSA topics.
# This ensures that the automated commits generate REAL, high-value technical documentation.
TOPICS = [
    {
        "title": "Consistent Hashing in Distributed Systems",
        "category": "System Design",
        "summary": "Consistent hashing minimizes key redistribution when scaling node counts. By mapping both keys and nodes to a circular space (the hash ring), adding or removing a node only impacts k/n keys. Virtual nodes are utilized to distribute load evenly across heterogeneous physical servers."
    },
    {
        "title": "Log-Structured Merge-Trees (LSM Trees)",
        "category": "Storage Engines",
        "summary": "LSM Trees optimize for write-heavy workloads by writing sequentially to a memory buffer (MemTable). Once full, it flushes to disk as an immutable SSTable (Sorted String Table). Reads query the MemTable and then SSTables via Bloom filters, relying on background Compaction to merge duplicate updates."
    },
    {
        "title": "Write-Ahead Logging (WAL) and Durability",
        "category": "Database Internals",
        "summary": "WAL guarantees durability and atomicity by requiring all modifications to be logged sequentially in non-volatile storage before they are applied to the database pages. In the event of a crash, the log is replayed (Redo/Undo phases) to restore database consistency."
    },
    {
        "title": "Asynchronous Concurrency: Thread Pools vs Event Loops",
        "category": "Concurrency Systems",
        "summary": "Multi-threaded systems handle concurrency by spawning a thread per request, risking high context-switch overhead under load. Event loops (like Python's asyncio or Node.js) run on a single thread, using non-blocking I/O multiplexing (epoll/kqueue) to yield control while waiting on network packets."
    },
    {
        "title": "Optimistic vs Pessimistic Concurrency Control",
        "category": "Database Transactions",
        "summary": "Pessimistic locking prevents conflicts by acquiring shared or exclusive locks on data before modification, risking deadlocks. Optimistic locking assumes conflicts are rare, checking if data has been modified by another transaction (via version numbers or timestamps) before committing, retrying if a conflict is detected."
    },
    {
        "title": "Kafka Partitioning and Consumer Group Rebalancing",
        "category": "Data Streaming",
        "summary": "Kafka achieves scale by partitioning topics. A consumer group distributes partitions among active consumer instances. If a consumer fails or joins, a rebalance occurs. Using static membership and cooperative sticky assignors reduces rebalance latency and minimizes message processing gaps."
    },
    {
        "title": "Star Schema vs Snowflake Schema in Data Warehouses",
        "category": "Data Modeling",
        "summary": "A star schema contains a central fact table joined to denormalized dimension tables, optimizing for fast read queries with minimal joins. A snowflake schema normalizes dimension tables into secondary tables, reducing data redundancy at the cost of query performance due to extra joins."
    },
    {
        "title": "Bloom Filters: Space-Efficient Probabilistic Sets",
        "category": "Data Structures",
        "summary": "A Bloom filter is a space-efficient bit array representing a set. It uses multiple hash functions to set bits on insert. Queries check if all bits are set; a negative response guarantees the element is not in the set, while a positive response carries a configurable false-positive probability."
    },
    {
        "title": "CAP Theorem: PACELC Extension",
        "category": "Distributed Systems",
        "summary": "While CAP states a system can only guarantee 2 of Consistency, Availability, or Partition Tolerance, PACELC extends this: If there is a Partition (P), trade off Availability (A) or Consistency (C); Else (E), trade off Latency (L) or Consistency (C) (e.g., MongoDB yields consistency for latency under normal operation)."
    },
    {
        "title": "SSTable Compaction: Size-Tiered vs Leveled",
        "category": "Storage Engines",
        "summary": "Size-tiered compaction groups similarly sized SSTables and merges them into larger ones, risking high disk write-amplification. Leveled compaction divides disk into layers (L1, L2...), where each layer has a non-overlapping key space. It keeps read amplification low but requires constant merge operations."
    },
    {
        "title": "Idempotency Keys in Payment & API Gateway Design",
        "category": "API Architecture",
        "summary": "To prevent duplicate transactions, client requests include a unique idempotency key. The server stores this key along with the response in a cache (e.g. Redis) with a TTL. If a retry with the same key is received, the server returns the cached response directly instead of re-executing the operation."
    },
    {
        "title": "Redis Event Loop & Memory Eviction Policies",
        "category": "Caching Systems",
        "summary": "Redis is single-threaded, using non-blocking socket multiplexing via an event library (ae) to handle thousands of operations/sec. When max memory is reached, eviction policies like volatile-lru (Least Recently Used), allkeys-lfu (Least Frequently Used), or random eviction free up memory."
    }
]

def run_log():
    # Setup directories
    os.makedirs("logs", exist_ok=True)
    
    # Pick a random topic to simulate actual study logs
    topic = random.choice(TOPICS)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"logs/{date_str}.md"
    
    # Create the daily study log
    content = f"""# Today I Learned - {date_str}
    
## Category: {topic['category']}
### **{topic['title']}**

{topic['summary']}

---
*Auto-logged via GitHub Actions on {date_str}*
"""
    
    with open(log_filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Log generated successfully: {log_filename}")
    
    # Append to README.md history table
    readme_content = ""
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
            
    history_line = f"| {date_str} | **{topic['category']}** | [{topic['title']}](./{log_filename}) |\n"
    
    if "## 📅 Logs History" not in readme_content:
        readme_content = f"""# 📚 Systems Engineering & DSA Log

Automated workspace for logging daily study patterns, system design trade-offs, and algorithm templates. Powered by GitHub Actions.

## 📅 Logs History
| Date | Category | Topic |
|---|---|---|
"""
    
    # Check if the date is already logged to prevent duplicates on manual trigger
    if date_str not in readme_content:
        readme_content += history_line
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(readme_content)
            
if __name__ == "__main__":
    run_log()
