---

# **🚨 Postmortem: Bank Fee Transparency Tool Outage**  

## **🛑 Issue Summary**  
- **📅 Duration:** February 25, 2025, 14:10 - 16:45 WAT (2 hours, 35 minutes)  
- **💥 Impact:**  
  - **100% downtime** – Users could not access the platform.  
  - **Users encountered** `500 Internal Server Error` on all pages.  
- **🔍 Root Cause:**  
  - Misconfigured PostgreSQL connection pool exhausted available connections, causing backend failure.  

---

## **📜 Timeline**  

| Time (WAT) | Event |
|------------|--------|
| **14:10** | System monitoring alerts triggered due to high database connection usage. |
| **14:15** | First user complaints received via support. |
| **14:25** | Engineers investigate logs, suspecting a backend issue. |
| **14:40** | Restarted backend services; issue persisted. |
| **14:55** | PostgreSQL logs reveal connection pool exhaustion. |
| **15:10** | Initial assumption: high traffic spike. |
| **15:30** | Query analysis shows **no unusual traffic**. |
| **15:50** | Root cause identified: **unclosed database connections**. |
| **16:10** | Fixed connection pool settings, redeployed backend. |
| **16:45** | System fully restored and monitored for stability. |

---

## **⚙️ Root Cause and Fix**  

### **🔎 Root Cause**  
- The Node.js backend used `pg-pool`, but connections **were not released** properly.  
- The database reached its **max connection limit**, causing new queries to fail.  

### **🛠️ Resolution**  
✅ Adjusted connection pooling settings to **close idle connections**.  
✅ Implemented a **timeout mechanism** for stale connections.  
✅ Redeployed the backend with the new configuration.  

---

## **🚀 Preventative Measures**  

### **💡 Improvements Needed**  
- Better **database connection handling** to prevent exhaustion.  
- **Stronger monitoring** for early connection leak detection.  
- **Circuit breakers** to gracefully handle database failures.  

### **📝 Action Items (TODO)**  
- [ ] **Patch connection pooling logic** to release unused connections.  
- [ ] **Add monitoring alerts** for high database connection usage.  
- [ ] **Implement request throttling** to prevent excessive DB connections.  
- [ ] **Run load tests** to simulate high traffic and validate fixes.

---
